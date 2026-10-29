import json
import tempfile
import unittest
import zipfile
from pathlib import Path
from unittest.mock import patch

from skill_package import check, diff, install, pack, seal, snapshot
from wiki_exporter.lark import ExportError


class SkillPackageTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        self.source = self.root / "source" / "example-guide"
        self.source.mkdir(parents=True)
        (self.source / "SKILL.md").write_text(
            '---\nname: example-guide\ndescription: A fixture.\nmetadata:\n  version: "1.0.0"\n---\n\n[Use](references/use.md)\n'
        )
        (self.source / "references").mkdir()
        (self.source / "references/use.md").write_text("Original reference.\n")
        seal(self.source)
        self.dest = self.root / "host/skills"
        self.backup = self.root / "backup"

    def upgrade(self):
        p = self.source / "SKILL.md"
        p.write_text(p.read_text().replace('"1.0.0"', '"1.1.0"'))
        (self.source / "references/use.md").write_text("Updated reference.\n")
        seal(self.source)

    def test_reproducible_portable_archive_and_tamper_detection(self):
        a = pack(self.source, self.root / "one")
        b = pack(self.source, self.root / "two")
        self.assertEqual(a["sha256"], b["sha256"])
        with zipfile.ZipFile(a["archive"]) as archive:
            archive.extractall(self.root / "unpacked")
        self.assertEqual(check(self.root / "unpacked/example-guide"), check(self.source))
        (self.source / "references/use.md").write_text("Unreviewed change")
        with self.assertRaises(ExportError):
            pack(self.source, self.root / "three")

    def test_broken_link_escape_and_symlink_are_rejected(self):
        p = self.source / "references/use.md"
        for text in ("[Missing](missing.md)", "[Outside](../../outside.md)"):
            p.write_text(text)
            with self.assertRaises(ExportError):
                seal(self.source)
        p.unlink()
        (self.root / "outside.md").write_text("Outside")
        p.symlink_to(self.root / "outside.md")
        with self.assertRaises(ExportError):
            seal(self.source)

    def test_install_update_preserves_backup_and_unrelated_skills(self):
        unrelated = self.dest / "my-work"
        unrelated.mkdir(parents=True)
        (unrelated / "notes.md").write_text("Keep me")
        install(self.source, self.dest)
        old = snapshot(self.dest / "example-guide")
        self.upgrade()
        result = install(self.source, self.dest, backup=self.backup)
        self.assertEqual(snapshot(Path(result["backup"]) / "example-guide"), old)
        self.assertEqual(check(self.dest / "example-guide"), check(self.source))
        self.assertEqual((unrelated / "notes.md").read_text(), "Keep me")
        self.assertTrue(install(self.source, self.dest)["already_current"])

    def test_modified_install_requires_explicit_archival(self):
        install(self.source, self.dest)
        local = self.dest / "example-guide/references/use.md"
        local.write_text("My personal changes")
        self.upgrade()
        with self.assertRaises(ExportError):
            install(self.source, self.dest, backup=self.backup)
        self.assertEqual(local.read_text(), "My personal changes")
        result = install(self.source, self.dest, backup=self.backup, archive_existing=True)
        self.assertEqual((Path(result["backup"]) / "example-guide/references/use.md").read_text(), "My personal changes")

    def test_legacy_migration_dry_run_and_backup_outside_discovery(self):
        for name in ("example-guide", "old-overview"):
            p = self.dest / name
            p.mkdir(parents=True)
            (p / "SKILL.md").write_text("Original authored text and examples")
        before = snapshot(self.dest)
        result = install(self.source, self.dest, backup=self.backup, archive_existing=True,
                         retire=("old-overview",), dry_run=True)
        self.assertTrue(result["dry_run"])
        self.assertEqual(snapshot(self.dest), before)
        self.assertFalse(self.backup.exists())
        with self.assertRaises(ExportError):
            install(self.source, self.dest, backup=self.dest / "backups", archive_existing=True)
        result = install(self.source, self.dest, backup=self.backup, archive_existing=True,
                         retire=("old-overview",))
        self.assertFalse((self.dest / "old-overview").exists())
        self.assertEqual((Path(result["backup"]) / "old-overview/SKILL.md").read_text(),
                         "Original authored text and examples")

    def test_publish_failure_restores_previous_install(self):
        install(self.source, self.dest)
        before = snapshot(self.dest / "example-guide")
        self.upgrade()
        rename = Path.rename

        def fail_publication(path, destination):
            if path.name == "example-guide" and path.parent.name.startswith(".skill-install-"):
                raise OSError("Synthetic rename failure")
            return rename(path, destination)

        with patch.object(Path, "rename", fail_publication):
            with self.assertRaises(OSError):
                install(self.source, self.dest, backup=self.backup)
        self.assertEqual(snapshot(self.dest / "example-guide"), before)

    def test_same_version_cannot_change_an_existing_release(self):
        pack(self.source, self.root / "dist")
        (self.source / "references/use.md").write_text("Different bytes, same version")
        seal(self.source)
        with self.assertRaises(ExportError):
            pack(self.source, self.root / "dist")

    def test_diff_reads_legacy_without_rewriting_it(self):
        old = self.root / "legacy"
        old.mkdir()
        (old / "SKILL.md").write_text("Human example\n")
        before = snapshot(old)
        result = diff(old, self.source)
        self.assertIn("Human example", result)
        self.assertIn("references/use.md", result)
        self.assertEqual(snapshot(old), before)

    def test_invalid_installed_manifest_is_preserved_until_explicit_archival(self):
        install(self.source, self.dest)
        bad = self.dest / "example-guide/manifest.json"
        bad.write_text(json.dumps(["invalid manifest"]))
        before = snapshot(self.dest / "example-guide")
        self.upgrade()
        with self.assertRaises(ExportError):
            install(self.source, self.dest, backup=self.backup)
        self.assertEqual(snapshot(self.dest / "example-guide"), before)
        result = install(self.source, self.dest, backup=self.backup, archive_existing=True)
        self.assertEqual(snapshot(Path(result["backup"]) / "example-guide"), before)

    def test_repository_package_can_be_read_without_other_skill_bundles(self):
        source = Path(__file__).resolve().parents[1] / "skills/sai-user-guide"
        result = pack(source, self.root / "published")
        with zipfile.ZipFile(result["archive"]) as archive:
            archive.extractall(self.root / "clean-client")
        copied = self.root / "clean-client/sai-user-guide"
        self.assertEqual(check(copied), check(source))

    def test_open_editor_can_save_into_retired_original_after_update(self):
        install(self.source, self.dest)
        old_file = self.dest / "example-guide/references/use.md"
        self.upgrade()
        with old_file.open("a") as editor:
            result = install(self.source, self.dest, backup=self.backup)
            editor.write("Saved through an open editor after the update.\n")
            editor.flush()
        archived = Path(result["backup"]) / "example-guide/references/use.md"
        self.assertIn("Saved through an open editor", archived.read_text())
        self.assertEqual(old_file.read_text(), "Updated reference.\n")

    def test_manifest_edit_during_failed_readback_is_not_deleted(self):
        install(self.source, self.dest)
        self.upgrade()
        target = self.dest / "example-guide"

        def read_and_edit(path):
            result = check(path)
            if path == target and result["version"] == "1.1.0":
                (target / "manifest.json").write_text("A concurrently saved manifest")
                raise ExportError("Synthetic readback failure")
            return result

        with patch("skill_package.check", side_effect=read_and_edit):
            with self.assertRaises(ExportError):
                install(self.source, self.dest, backup=self.backup)
        self.assertEqual((target / "manifest.json").read_text(), "A concurrently saved manifest")
        archives = list(self.backup.glob("*/example-guide"))
        self.assertEqual(len(archives), 1)
        self.assertEqual(check(archives[0])["version"], "1.0.0")


if __name__ == "__main__":
    unittest.main()
