#!/usr/bin/env python3
"""Install this checkout's tracked Beads/report hooks using a portable path."""
from __future__ import annotations

import os
from pathlib import Path
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[1]


def install(root: Path) -> None:
    hooks = root / ".beads/hooks"
    pre_commit = hooks / "pre-commit"
    if not pre_commit.is_file() or "scripts/report_ci.py" not in pre_commit.read_text():
        raise RuntimeError("The tracked .beads/hooks/pre-commit report integration is missing. Restore the repository hook before installing.")
    current = subprocess.run(["git", "config", "--local", "--get", "core.hooksPath"], cwd=root,
                             capture_output=True, text=True, timeout=30)
    if current.returncode not in {0, 1}:
        raise RuntimeError(current.stderr.strip() or "Cannot read the Git hook configuration.")
    configured = current.stdout.strip()
    if configured:
        path = Path(os.path.expanduser(configured))
        absolute = path if path.is_absolute() else root / path
        if absolute.resolve() != hooks.resolve():
            raise RuntimeError(f"A different custom hooksPath is configured: {configured}. Integrate the report hook there or explicitly select .beads/hooks; this installer will not replace it silently.")
    for hook in hooks.iterdir():
        if hook.is_file() and not hook.name.startswith("."):
            hook.chmod(hook.stat().st_mode | 0o111)
    subprocess.run(["git", "config", "--local", "core.hooksPath", ".beads/hooks"], cwd=root,
                   check=True, timeout=30)
    print("Installed portable .beads/hooks; Beads integration is preserved and report checks require no bd executable.")


def main() -> int:
    try:
        install(ROOT)
    except (RuntimeError, OSError, subprocess.SubprocessError) as error:
        print("Hook installation failed: " + str(error), file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
