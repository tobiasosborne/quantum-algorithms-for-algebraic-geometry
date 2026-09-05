"""Real temporary Git-index regressions; report rendering is stubbed, never science."""
from __future__ import annotations

import importlib.util
import os
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
import unittest
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[2]


def load(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


ci = load("qaag_report_ci", ROOT / "scripts/report_ci.py")
installer = load("qaag_install_hooks", ROOT / "scripts/install_hooks.py")


class StagedReportTests(unittest.TestCase):
    def setUp(self):
        # Git exports repository/index selectors to hooks, including temporary
        # indexes for partial commits. None may reach an isolated fixture repo.
        clean_environment = {key: value for key, value in os.environ.items() if not key.startswith("GIT_")}
        environment_patch = patch.dict(os.environ, clean_environment, clear=True)
        environment_patch.start()
        self.addCleanup(environment_patch.stop)
        self.temporary = tempfile.TemporaryDirectory(prefix="qaag-hook-test-")
        self.addCleanup(self.temporary.cleanup)
        self.repo = Path(self.temporary.name)
        self.git("init", "--quiet")
        self.git("config", "user.name", "Report CI fixture")
        self.git("config", "user.email", "fixture@example.invalid")
        for path, text in {
            "scouting/example.md": "version one\n",
            "reports/content/routes.json": "[]\n",
            "reports/report.template.html": "<article>fixture</article>\n",
            ci.ARTIFACT: "rendered:version one\n",
            "README.md": "original readme\n",
            "notes.txt": "unrelated original\n",
        }.items():
            self.write(path, text)
        self.git("add", "--all")
        self.git("-c", "core.hooksPath=/dev/null", "commit", "--quiet", "-m", "fixture baseline")

    def git(self, *args):
        return subprocess.run(["git", *args], cwd=self.repo, check=True, capture_output=True,
                              text=True, timeout=30).stdout

    def write(self, path, text):
        target = self.repo / path
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(text)

    def stage_source(self):
        self.write("scouting/example.md", "version two\n")
        self.git("add", "--", "scouting/example.md")

    def fake_pipeline(self, root, mode):
        self.assertEqual(root, self.repo)
        self.assertEqual(mode, "ci")
        self.write(ci.ARTIFACT, "rendered:" + (root / "scouting/example.md").read_text())

    def test_stale_report_is_regenerated_without_bundling_unrelated_edits(self):
        self.stage_source()
        self.write("README.md", "staged readme\n")
        self.git("add", "--", "README.md")
        self.write("README.md", "unstaged readme refinement\n")
        self.write("notes.txt", "private unfinished notes\n")
        self.write("scratch.txt", "untracked unrelated\n")
        with patch.object(ci, "run_pipeline", side_effect=self.fake_pipeline):
            ci.pre_commit(self.repo)
        self.assertEqual(self.git("show", ":" + ci.ARTIFACT), "rendered:version two\n")
        self.assertEqual(self.git("show", ":README.md"), "staged readme\n")
        self.assertEqual((self.repo / "README.md").read_text(), "unstaged readme refinement\n")
        self.assertEqual(self.git("show", ":notes.txt"), "unrelated original\n")
        self.assertEqual((self.repo / "notes.txt").read_text(), "private unfinished notes\n")
        self.assertNotIn("scratch.txt", self.git("ls-files"))
        self.assertEqual(set(self.git("diff", "--cached", "--name-only").splitlines()),
                         {"README.md", "scouting/example.md", ci.ARTIFACT})

    def test_partial_scientific_staging_fails_before_build(self):
        self.stage_source()
        self.write("scouting/example.md", "unstaged third version\n")
        before = self.git("write-tree")
        with patch.object(ci, "run_pipeline") as pipeline:
            with self.assertRaisesRegex(ci.ReportCIError, "scouting/example.md"):
                ci.pre_commit(self.repo)
            pipeline.assert_not_called()
        self.assertEqual(before, self.git("write-tree"))
        self.assertEqual(self.git("show", ":scouting/example.md"), "version two\n")
        self.assertEqual((self.repo / ci.ARTIFACT).read_text(), "rendered:version one\n")

    def test_untracked_scientific_input_fails_before_build(self):
        self.stage_source()
        self.write("scouting/new-route.md", "not staged\n")
        with patch.object(ci, "run_pipeline") as pipeline:
            with self.assertRaisesRegex(ci.ReportCIError, "scouting/new-route.md"):
                ci.pre_commit(self.repo)
            pipeline.assert_not_called()

    def test_readme_commit_skips_even_with_unfinished_inventory(self):
        self.write("README.md", "documentation change\n")
        self.git("add", "--", "README.md")
        self.write("reports/content/routes.json", "unfinished JSON {")
        with patch.object(ci, "run_pipeline") as pipeline:
            ci.pre_commit(self.repo)
            pipeline.assert_not_called()

    def test_failed_validation_never_stages_generated_artifact(self):
        self.stage_source()
        before = self.git("write-tree")
        def failed(root, mode):
            self.fake_pipeline(root, mode)
            raise ci.ReportCIError("deliberate verifier failure")
        with patch.object(ci, "run_pipeline", side_effect=failed):
            with self.assertRaisesRegex(ci.ReportCIError, "deliberate verifier failure"):
                ci.pre_commit(self.repo)
        self.assertEqual(before, self.git("write-tree"))
        self.assertEqual(self.git("show", ":" + ci.ARTIFACT), "rendered:version one\n")

    def test_concurrent_index_change_is_not_overwritten(self):
        self.stage_source()
        def changed(root, mode):
            self.fake_pipeline(root, mode)
            self.write("README.md", "concurrently staged\n")
            self.git("add", "--", "README.md")
        with patch.object(ci, "run_pipeline", side_effect=changed):
            with self.assertRaisesRegex(ci.ReportCIError, "index changed"):
                ci.pre_commit(self.repo)
        self.assertEqual(self.git("show", ":README.md"), "concurrently staged\n")
        self.assertEqual(self.git("show", ":" + ci.ARTIFACT), "rendered:version one\n")

    def test_artifact_only_change_is_checked(self):
        self.write(ci.ARTIFACT, "deliberately stale HTML\n")
        self.git("add", "--", ci.ARTIFACT)
        with patch.object(ci, "run_pipeline", side_effect=self.fake_pipeline):
            ci.pre_commit(self.repo)
        self.assertEqual(self.git("show", ":" + ci.ARTIFACT), "rendered:version one\n")

    def test_installer_preserves_beads_and_hook_runs_without_bd(self):
        hook = self.repo / ".beads/hooks/pre-commit"
        original = (ROOT / ".beads/hooks/pre-commit").read_text()
        self.write(".beads/hooks/pre-commit", original)
        self.write("scripts/report_ci.py", (ROOT / "scripts/report_ci.py").read_text())
        hook.chmod(0o644)
        self.git("config", "core.hooksPath", str(hook.parent))
        installer.install(self.repo)
        self.assertEqual(hook.read_text(), original)
        self.assertTrue(os.access(hook, os.X_OK))
        self.assertEqual(self.git("config", "--get", "core.hooksPath").strip(), ".beads/hooks")
        command_bin = self.repo / "fixture-bin"
        command_bin.mkdir()
        for name, executable in {"sh": shutil.which("sh"), "git": shutil.which("git"), "python3": sys.executable}.items():
            (command_bin / name).symlink_to(executable)
        env = dict(os.environ, PATH=str(command_bin))
        result = subprocess.run([str(hook)], cwd=self.repo, env=env, capture_output=True, text=True, timeout=30)
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn("report checks skipped", result.stdout)

    def test_installer_keeps_different_custom_hook_configuration(self):
        self.write(".beads/hooks/pre-commit", (ROOT / ".beads/hooks/pre-commit").read_text())
        self.git("config", "core.hooksPath", "custom-hooks")
        with self.assertRaisesRegex(RuntimeError, "different custom hooksPath"):
            installer.install(self.repo)
        self.assertEqual(self.git("config", "--get", "core.hooksPath").strip(), "custom-hooks")


if __name__ == "__main__":
    unittest.main()
