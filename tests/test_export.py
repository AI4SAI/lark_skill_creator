import base64
import json
import os
import shutil
import subprocess
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

from generate_skills import build
from wiki_exporter.bundle import read_manifest
from wiki_exporter.lark import ExportError, Lark
from wiki_exporter.wiki_exporter import export


def response(data, *, ok=True, returncode=0):
    return subprocess.CompletedProcess(
        [], returncode, json.dumps({"ok": ok, "data": data}), "private diagnostic"
    )


class CliTests(unittest.TestCase):
    def test_pagination_and_user_identity(self):
        first = [{"node_token": f"node-{n}"} for n in range(50)]
        with patch(
            "wiki_exporter.lark.subprocess.run",
            side_effect=[
                response({"nodes": first, "has_more": True, "page_token": "next"}),
                response({"nodes": [{"node_token": "node-50"}], "has_more": False}),
            ],
        ) as run:
            self.assertEqual(len(Lark(Path.cwd()).nodes("space")), 51)
            self.assertIn("next", run.call_args.args[0])
            self.assertEqual(
                run.call_args.args[0][-4:], ["--as", "user", "--format", "json"]
            )

    def test_error_and_stalled_cursor_do_not_become_empty_success(self):
        for result in (
            response({}, ok=False),
            response({}, returncode=1),
            response({}),
        ):
            with (
                self.subTest(result=result.returncode),
                patch("wiki_exporter.lark.subprocess.run", return_value=result),
            ):
                with self.assertRaises(ExportError) as caught:
                    Lark(Path.cwd()).nodes("space")
                self.assertNotIn("private diagnostic", str(caught.exception))
        page = response({"nodes": [], "has_more": True, "page_token": "same"})
        with (
            patch("wiki_exporter.lark.subprocess.run", return_value=page),
            self.assertRaises(ExportError),
        ):
            Lark(Path.cwd()).nodes("space")

    def test_pending_export_polls_the_existing_ticket(self):
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            target = root / "source.docx"
            calls = []

            def call(*args):
                calls.append(args)
                if args[1] == "+export":
                    return {"ticket": "existing-ticket", "ready": False}
                if args[1] == "+task_result":
                    return {"file_token": "exported-file", "job_status": 0}
                target.write_bytes(b"downloaded native file")
                return {"downloaded": True}

            client = Lark(root)
            with patch.object(client, "call", side_effect=call):
                client.export_docx("document", target, 3)
            self.assertEqual(
                [c[1] for c in calls], ["+export", "+task_result", "+export-download"]
            )
            self.assertIn("existing-ticket", calls[1])

    def test_timeout_resumes_original_ticket_and_revision(self):
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            target = root / "source.docx"
            client = Lark(root)
            with (
                patch.object(
                    client,
                    "call",
                    side_effect=[{"ticket": "original-ticket"}]
                    + [{"job_status": 2}] * 30,
                ),
                patch("wiki_exporter.lark.time.sleep"),
                self.assertRaises(ExportError),
            ):
                client.export_docx("document", target, 3)
            checkpoint = next((root / ".lark-export-tasks").glob("*.json"))
            self.assertEqual(checkpoint.stat().st_mode & 0o777, 0o600)
            self.assertEqual(json.loads(checkpoint.read_text())["revision"], 3)
            calls = []

            def resume(*args):
                calls.append(args)
                if args[1] == "+task_result":
                    return {"file_token": "exported-file", "job_status": 0}
                target.write_bytes(b"original version")
                return {"downloaded": True}

            with patch.object(client, "call", side_effect=resume):
                self.assertEqual(client.export_docx("document", target, 4), 3)
            self.assertEqual(
                [c[1] for c in calls], ["+task_result", "+export-download"]
            )
            self.assertIn("original-ticket", calls[0])
            self.assertFalse(checkpoint.exists())


class FixtureLark:
    def __init__(self, root, files):
        self.cwd, self.files = root, files
        self.drift = False
        self.calls = {}
        self.deleted = False
        self.title = "相同标题"

    def nodes(self, space, parent):
        if parent:
            return []
        return [
            {
                "node_token": "node-" + label,
                "obj_token": "doc-" + label,
                "obj_type": "docx",
                "title": self.title,
                "has_child": False,
            }
            for label in ("a",)
            if self.deleted
        ] or [
            {
                "node_token": "node-" + label,
                "obj_token": "doc-" + label,
                "obj_type": "docx",
                "title": self.title,
                "has_child": False,
            }
            for label in ("a", "b")
        ]

    def document(self, token):
        self.calls[token] = self.calls.get(token, 0) + 1
        revision = self.calls[token] if self.drift else 3
        return {
            "revision_id": revision,
            "content": '<title>Guide</title><source token="file" name="example.html"/>',
        }

    def export_docx(self, token, destination, revision):
        shutil.copyfile(self.files[token], destination)
        return revision

    def attachment(self, token, destination):
        destination.write_bytes(b"<html>synthetic attachment</html>")


@unittest.skipUnless(
    os.environ.get("PANDOC") or shutil.which("pandoc"), "real Pandoc required"
)
class ConversionTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.temp = tempfile.TemporaryDirectory()
        cls.root = Path(cls.temp.name)
        cls.pandoc = os.environ.get("PANDOC") or shutil.which("pandoc")
        (cls.root / "pixel.png").write_bytes(
            base64.b64decode(
                "iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAQAAAC1HAwCAAAAC0lEQVR42mP8/x8AAwMCAO+/l9sAAAAASUVORK5CYII="
            )
        )
        cls.long_text = "内容需要原样保留。" * 16000 + "最后一句应保留。"
        bodies = {
            "a": "# 第一页\n\n[第二页](https://example.feishu.cn/wiki/node-b)\n\n"
            "![说明图](pixel.png)\n\n| 名称 | 值 |\n|---|---|\n| CPU | 4 |\n\n"
            "```bash\nprintf 'example'\n```\n\n" + cls.long_text,
            "b": "# 第二页\n\n短文。",
        }
        cls.files = {}
        for label, text in bodies.items():
            path = cls.root / (label + ".docx")
            subprocess.run(
                [cls.pandoc, "--from=gfm", "--to=docx", "--output", str(path)],
                input=text,
                text=True,
                cwd=cls.root,
                check=True,
                capture_output=True,
            )
            cls.files["doc-" + label] = path

    @classmethod
    def tearDownClass(cls):
        cls.temp.cleanup()

    def setUp(self):
        self.workspace = tempfile.TemporaryDirectory()
        self.addCleanup(self.workspace.cleanup)
        self.work = Path(self.workspace.name)
        self.source = self.work / "export"
        self.lark = FixtureLark(self.work, self.files)
        export(self.lark, "space", self.source, pandoc=self.pandoc)

    def review(self, page_ids):
        review = self.work / "review.json"
        review.write_text(
            json.dumps(
                {
                    "content_sha256": read_manifest(self.source)["content_sha256"],
                    "skills": [
                        {
                            "name": "example-guide",
                            "description": "Read the reviewed example guide.",
                            "pages": page_ids,
                        }
                    ],
                }
            )
        )
        return review

    def test_images_tables_long_short_documents_and_links_survive(self):
        manifest = read_manifest(self.source)
        self.assertEqual(len(manifest["pages"]), 2)
        first, second = manifest["pages"]
        text = (self.source / "content" / first["path"]).read_text()
        self.assertIn(self.long_text, text)
        self.assertIn("printf 'example'", text)
        self.assertIn("| CPU", text)
        self.assertIn("../" + second["path"], text)
        self.assertIn('download="example.html"', text)
        self.assertTrue(
            list((self.source / "content" / first["page_id"] / "assets").rglob("*.png"))
        )
        self.assertIn("短文", (self.source / "content" / second["path"]).read_text())
        self.assertEqual(first["dependencies"], [second["page_id"]])
        output = self.work / "published"
        build(self.source, self.review([first["page_id"], second["page_id"]]), output)
        for path in (output / "site").rglob("*"):
            if path.is_file():
                relative = path.relative_to(output / "site")
                self.assertEqual(
                    path.read_bytes(),
                    (
                        output / "skills/example-guide/references" / relative
                    ).read_bytes(),
                )
        skill = (output / "skills/example-guide/SKILL.md").read_text()
        self.assertLess(len(skill), 1500)

    def test_missing_review_revision_drift_and_manual_edits_preserve_outputs(self):
        pages = read_manifest(self.source)["pages"]
        with self.assertRaises(ExportError):
            build(self.source, self.review([pages[0]["page_id"]]), self.work / "bad")
        before = (self.source / "manifest.json").read_bytes()
        self.lark.drift = True
        with self.assertRaises(ExportError):
            export(self.lark, "space", self.source, pandoc=self.pandoc, replace=True)
        self.assertEqual((self.source / "manifest.json").read_bytes(), before)
        self.lark.drift = False
        page = self.source / "content" / pages[0]["path"]
        page.write_text("manual change")
        with self.assertRaises(ExportError):
            export(self.lark, "space", self.source, pandoc=self.pandoc, replace=True)
        self.assertEqual(page.read_text(), "manual change")

    def test_rename_and_deletion_remove_stale_generated_pages(self):
        before = read_manifest(self.source)
        removed = before["pages"][1]["page_id"]
        self.lark.deleted = True
        self.lark.title = "改名后的标题"
        export(self.lark, "space", self.source, pandoc=self.pandoc, replace=True)
        after = read_manifest(self.source)
        self.assertEqual(after["pages"][0]["page_id"], before["pages"][0]["page_id"])
        self.assertEqual(after["pages"][0]["title"], "改名后的标题")
        self.assertFalse((self.source / "content" / removed).exists())

    def test_unchanged_content_reuses_review_and_paths_cannot_overlap(self):
        manifest = read_manifest(self.source)
        review = self.review([page["page_id"] for page in manifest["pages"]])
        export(self.lark, "space", self.source, pandoc=self.pandoc, replace=True)
        self.assertEqual(
            read_manifest(self.source)["content_sha256"], manifest["content_sha256"]
        )
        build(self.source, review, self.work / "published")
        with self.assertRaises(ExportError):
            build(self.source, review, self.source / "child" / "..")
        alias = self.work / "alias"
        alias.symlink_to(self.source, target_is_directory=True)
        with self.assertRaises(ExportError):
            build(alias, review, self.work / "second")

    def test_changed_review_does_not_replace_published_content(self):
        manifest = read_manifest(self.source)
        review = self.review([page["page_id"] for page in manifest["pages"]])
        output = self.work / "published"
        build(self.source, review, output)
        previous = read_manifest(output)
        copytree = shutil.copytree

        def copy_and_edit(*args, **kwargs):
            result = copytree(*args, **kwargs)
            review.write_text(review.read_text() + "\n")
            return result

        with (
            patch("generate_skills.shutil.copytree", side_effect=copy_and_edit),
            self.assertRaisesRegex(ExportError, "审核记录发生变化"),
        ):
            build(self.source, review, output, replace=True)
        self.assertEqual(read_manifest(output), previous)

    def test_dynamic_blocks_and_old_export_cannot_be_published(self):
        before = read_manifest(self.source)
        with (
            patch.object(self.lark, "export_docx", return_value=2),
            self.assertRaisesRegex(ExportError, "旧版本导出"),
        ):
            export(self.lark, "space", self.source, pandoc=self.pandoc, replace=True)
        self.assertEqual(read_manifest(self.source), before)
        with patch.object(
            self.lark,
            "document",
            return_value={
                "revision_id": 3,
                "content": '<synced_reference token="example"/><task/>',
            },
        ):
            export(self.lark, "space", self.source, pandoc=self.pandoc, replace=True)
        manifest = read_manifest(self.source)
        self.assertTrue(all(page["warnings"] for page in manifest["pages"]))
        with self.assertRaisesRegex(ExportError, "转换警告"):
            build(
                self.source,
                self.review([page["page_id"] for page in manifest["pages"]]),
                self.work / "published",
            )


if __name__ == "__main__":
    unittest.main()
