#!/usr/bin/env python3
"""Explicit setup and bounded, offline report checks for local CI and Git hooks."""
from __future__ import annotations

import argparse
import json
import os
from pathlib import Path
import re
import shutil
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[1]
ARTIFACT = "reports/research-report.html"
COMMAND_TIMEOUT = 180
SETUP_TIMEOUT = 600
PYTHON_PACKAGES = {"Markdown": "3.5.2", "beautifulsoup4": "4.12.3"}
NODE_PACKAGES = {"katex": "0.16.22", "playwright": "1.55.0"}
FIXED_INPUTS = {
    "PRD.md", "HANDOFF.md", "LICENSE", "COPYING", "NOTICE", "Makefile",
    "reports/report.template.html", "reports/build_report.py", "reports/verify_report.cjs",
    "reports/package.json", "reports/package-lock.json", "reports/requirements.txt",
    "reports/THIRD_PARTY_NOTICES.md", "scripts/report_ci.py", "scripts/install_hooks.py",
    ".beads/hooks/pre-commit", "seed/page81.tex", "seed/page81.png",
}


class ReportCIError(RuntimeError):
    pass


def run(command: list[str], root: Path, *, capture: bool = False,
        env: dict[str, str] | None = None, timeout: int = COMMAND_TIMEOUT) -> str:
    try:
        result = subprocess.run(command, cwd=root, env=env, check=True,
                                stdout=subprocess.PIPE if capture else None,
                                stderr=subprocess.PIPE if capture else None,
                                timeout=timeout)
    except FileNotFoundError as error:
        raise ReportCIError(f"Required executable is unavailable: {command[0]}. Run make setup explicitly.") from error
    except subprocess.TimeoutExpired as error:
        raise ReportCIError(f"Command exceeded its {timeout}s limit: {' '.join(command)}") from error
    except subprocess.CalledProcessError as error:
        detail = (error.stderr or b"").decode("utf-8", "replace").strip() if capture else ""
        raise ReportCIError(f"Command failed ({error.returncode}): {' '.join(command)}" + (f"\n{detail}" if detail else "")) from error
    return result.stdout.decode("utf-8", "surrogateescape") if capture else ""


def git(root: Path, *arguments: str) -> str:
    return run(["git", *arguments], root, capture=True, timeout=30)


def filenames(root: Path, *arguments: str) -> set[str]:
    return {name for name in git(root, *arguments).split("\0") if name}


def declared_sources(root: Path) -> set[str]:
    """Read index declarations so unfinished work cannot affect unrelated commits."""
    result = set()
    inventories = filenames(root, "ls-files", "-z", "--", "reports/content")
    for path in sorted(path for path in inventories if path.endswith(".json")):
        try:
            records = json.loads(git(root, "show", ":" + path))
            result.update(source for record in records for source in record.get("sources", []) if isinstance(source, str))
        except (ValueError, AttributeError, TypeError) as error:
            raise ReportCIError(f"Cannot read staged report source inventory {path}: {error}") from error
    template = "reports/report.template.html"
    if template in filenames(root, "ls-files", "-z", "--", template):
        result.update(re.findall(r'data-source="([^"]+)"', git(root, "show", ":" + template)))
    # The report builder replaces this operational brief with HANDOFF.md.
    result.discard("briefs/problem-first-r8.md")
    return result


def is_report_input(path: str, declared: set[str]) -> bool:
    if path in FIXED_INPUTS or path in declared:
        return True
    parts = Path(path).parts
    if not parts:
        return False
    if parts[0] in {"scouting", "argument", "verdicts", "definitions", "claims", "refs"}:
        return Path(path).suffix.lower() in {".md", ".png", ".jpg", ".jpeg", ".gif", ".webp"}
    if parts[0] == "seed":
        return Path(path).suffix.lower() in {".md", ".py", ".tex", ".png", ".jpg", ".jpeg", ".gif", ".webp"}
    if parts[0] == "checkers":
        return Path(path).suffix.lower() in {".md", ".py"}
    if path.startswith("reports/content/"):
        return path.endswith(".json")
    return path.startswith("scripts/tests/") and path.endswith(".py") or path.startswith(".github/workflows/")


def require_clean_inputs(root: Path, declared: set[str]) -> None:
    unstaged = filenames(root, "diff", "--name-only", "--no-renames", "-z")
    untracked = filenames(root, "ls-files", "--others", "--exclude-standard", "-z")
    unsafe = sorted(path for path in unstaged | untracked if is_report_input(path, declared))
    if unsafe:
        listing = "\n".join("  " + path for path in unsafe)
        raise ReportCIError(
            "Report inputs contain unstaged or untracked changes:\n" + listing +
            "\nStage the intended complete versions, or move those edits out of the working tree, then retry. "
            "No files have been staged by this check. Partial scientific edits cannot be folded into the generated report."
        )


def find_python(root: Path) -> str:
    explicit = os.environ.get("QAAG_REPORT_PYTHON")
    candidates = [explicit] if explicit else [str(root / ".venv-report/bin/python3"), sys.executable, shutil.which("python3")]
    probe = "import json,importlib.metadata as m; print(json.dumps({p:m.version(p) for p in ['Markdown','beautifulsoup4']}))"
    errors = []
    for candidate in dict.fromkeys(p for p in candidates if p):
        if not Path(candidate).is_file() and not shutil.which(candidate):
            continue
        try:
            versions = json.loads(run([candidate, "-c", probe], root, capture=True, timeout=20))
            if versions == PYTHON_PACKAGES:
                return candidate
            errors.append(candidate + ": " + json.dumps(versions, sort_keys=True))
        except (ReportCIError, ValueError) as error:
            errors.append(str(error))
    raise ReportCIError("Pinned Python dependencies are unavailable. Run make setup explicitly, or set QAAG_REPORT_PYTHON to an interpreter with Markdown3.5.2 and beautifulsoup4 4.12.3.\n" + "\n".join(errors))


def find_package(root: Path, name: str) -> Path:
    explicit = os.environ.get("QAAG_KATEX_DIR") if name == "katex" else None
    candidates = [Path(explicit).expanduser()] if explicit else []
    candidates.extend([root / "reports/node_modules" / name, Path("/tmp/qaag-report-tools/node_modules") / name])
    for candidate in candidates:
        metadata = candidate / "package.json"
        if metadata.is_file():
            version = json.loads(metadata.read_text()).get("version")
            if version != NODE_PACKAGES[name]:
                raise ReportCIError(f"Expected {name} {NODE_PACKAGES[name]}, found {version} at {candidate}. Run make setup explicitly.")
            return candidate.resolve()
    raise ReportCIError(f"{name} {NODE_PACKAGES[name]} is unavailable. Run make setup explicitly; commits never install dependencies.")


def pipeline_environment(root: Path, *, browser: bool) -> dict[str, str]:
    env = dict(os.environ)
    env["PYTHONDONTWRITEBYTECODE"] = "1"
    env["QAAG_KATEX_DIR"] = str(find_package(root, "katex"))
    if browser:
        playwright = find_package(root, "playwright")
        explicit = env.get("QAAG_CHROMIUM_PATH")
        if explicit:
            executable = Path(explicit).expanduser().resolve()
            env["QAAG_CHROMIUM_PATH"] = str(executable)
        else:
            probe = "process.stdout.write(require(process.argv[1]).chromium.executablePath())"
            executable = Path(run(["node", "-e", probe, str(playwright)], root, capture=True, timeout=20).strip())
        if not executable.is_file() or not os.access(executable, os.X_OK):
            raise ReportCIError(
                f"Chromium is unavailable at {executable}. Run make setup-browser explicitly, "
                "or set QAAG_CHROMIUM_PATH to an installed Chromium executable. No download occurs during commits."
            )
    return env


def run_pipeline(root: Path, mode: str) -> None:
    python = find_python(root)
    browser = mode == "ci"
    env = pipeline_environment(root, browser=browser)
    builder = str(root / "reports/build_report.py")
    if mode in {"build", "ci"}:
        run([python, builder], root, env=env)
    if mode in {"check", "ci"}:
        run([python, builder, "--check"], root, env=env)
    if browser:
        if (root / "scripts/tests").is_dir():
            run([python, "-m", "unittest", "discover", "-s", "scripts/tests", "-v"], root, env=env)
        run(["node", str(root / "reports/verify_report.cjs")], root, env=env)


def pre_commit(root: Path) -> None:
    staged = filenames(root, "diff", "--cached", "--name-only", "--no-renames", "-z")
    declared = declared_sources(root)
    changed_inputs = sorted(path for path in staged if path == ARTIFACT or is_report_input(path, declared))
    if not changed_inputs:
        print("report-ci: no report inputs staged; report checks skipped.")
        return
    require_clean_inputs(root, declared)
    index_before = git(root, "write-tree").strip()
    print(f"report-ci: {len(changed_inputs)} staged report input(s); rebuilding and validating offline.", flush=True)
    run_pipeline(root, "ci")
    require_clean_inputs(root, declared_sources(root))
    if git(root, "write-tree").strip() != index_before:
        raise ReportCIError("The Git index changed while the report was building. Retry the commit after staging settles; the hook did not stage any files.")
    if not (root / ARTIFACT).is_file():
        raise ReportCIError("The report build did not produce " + ARTIFACT)
    git(root, "add", "--", ARTIFACT)
    print("report-ci: validated and staged only " + ARTIFACT)


def setup(root: Path) -> None:
    venv = root / ".venv-report"
    if not (venv / "bin/python3").is_file():
        run([sys.executable, "-m", "venv", str(venv)], root, timeout=SETUP_TIMEOUT)
    python = str(venv / "bin/python3")
    run([python, "-m", "pip", "--disable-pip-version-check", "install", "--requirement", "reports/requirements.txt"], root, timeout=SETUP_TIMEOUT)
    env = dict(os.environ, PLAYWRIGHT_SKIP_BROWSER_DOWNLOAD="1")
    run(["npm", "ci", "--prefix", "reports", "--no-audit", "--no-fund"], root, env=env, timeout=SETUP_TIMEOUT)
    run([sys.executable, str(root / "scripts/install_hooks.py")], root)
    print("report-ci: dependencies and portable hooks installed. Run make setup-browser if Chromium is not installed.")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("command", choices=["setup", "setup-browser", "build", "check", "ci", "pre-commit"])
    args = parser.parse_args()
    try:
        if args.command == "setup":
            setup(ROOT)
        elif args.command == "setup-browser":
            package = find_package(ROOT, "playwright")
            run(["node", str(package / "cli.js"), "install", "chromium"], ROOT, timeout=SETUP_TIMEOUT)
        elif args.command == "pre-commit":
            pre_commit(ROOT)
        else:
            run_pipeline(ROOT, args.command)
    except (ReportCIError, OSError, ValueError) as error:
        print("report-ci: " + str(error), file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
