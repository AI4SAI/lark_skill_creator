import base64
import html
import json
import os
import shutil
import subprocess
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

from PIL import Image

from generate_skills import build
from skill_package import check as check_skill, pack, seal
from wiki_exporter.bundle import read_manifest
from wiki_exporter.lark import ExportError, Lark
from wiki_exporter.wiki_exporter import export, wiki_source


def response(data, *, ok=True, returncode=0):
    return subprocess.CompletedProcess(
        [], returncode, json.dumps({"ok": ok, "data": data}), "private diagnostic"
    )


class CliTests(unittest.TestCase):
    def test_public_permission_requires_external_access_and_public_link(self):
        client = Lark(Path.cwd())
        for external, sharing, accepted in (
            (True, "anyone_readable", True), (True, "anyone_editable", True),
            (False, "anyone_readable", False), (True, "tenant_readable", False),
            (None, None, False),
        ):
            with self.subTest(external=external, sharing=sharing), patch.object(
                client, "call", return_value={"permission_public": {
                    "external_access": external, "link_share_entity": sharing,
                }}
            ):
                if accepted:
                    self.assertEqual(client.public_sharing("doc"), sharing)
                else:
                    with self.assertRaises(ExportError):
                        client.public_sharing("doc")

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

    def test_space_url_retains_its_tenant_for_document_references(self):
        self.assertEqual(
            wiki_source("https://example.feishu.cn/wiki/space/123"),
            ("123", "https://example.feishu.cn"),
        )
        self.assertEqual(wiki_source("123"), ("123", None))
        with self.assertRaises(ExportError):
            wiki_source("https://example.feishu.cn/docx/123")

    def test_full_native_structure_and_exact_referenced_block(self):
        client = Lark(Path.cwd())
        with patch.object(
            client,
            "call",
            return_value={"document": {"revision_id": 3, "content": "<p>Text</p>"}},
        ) as call:
            self.assertEqual(client.document("source", "block")["revision_id"], 3)
            args = call.call_args.args
            self.assertEqual(args[args.index("--detail") + 1], "full")
            self.assertEqual(args[args.index("--scope") + 1], "range")
            self.assertEqual(args[args.index("--start-block-id") + 1], "block")
            self.assertEqual(args[args.index("--end-block-id") + 1], "block")


class FixtureLark:
    def __init__(self, root, files):
        self.cwd, self.files = root, files
        self.drift = False
        self.calls = {}
        self.deleted = False
        self.title = "相同标题"

    def public_sharing(self, token):
        return "anyone_readable"

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

    def document(self, token, block=None):
        key = token + (":" + block if block else "")
        self.calls[key] = self.calls.get(key, 0) + 1
        return {
            "revision_id": self.calls[key] if self.drift else 3,
            "content": self.files[key],
        }

    def attachment(self, token, destination, *, kind="media"):
        if destination.suffix == ".bin":
            destination.write_bytes(b"<html>synthetic attachment</html>")
        else:
            destination.write_bytes(
                base64.b64decode(
                    "iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAQAAAC1HAwCAAAAC0lEQVR42mP8/x8AAwMCAO+/l9sAAAAASUVORK5CYII="
                )
            )


@unittest.skipUnless(
    os.environ.get("PANDOC") or shutil.which("pandoc"), "real Pandoc required"
)
class ConversionTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.pandoc = os.environ.get("PANDOC") or shutil.which("pandoc")
        cls.long_text = "内容需要原样保留。" * 16000 + "最后一句应保留。"
        # Native DocxXML shape, not a DOCX generated by Pandoc itself.
        cls.files = {
            "doc-a": "<title>第一页</title><h1>示例</h1>"
            '<p><cite doc-id="node-b" file-type="wiki" title="第二页"/></p>'
            '<callout emoji="⚠️"><p>重要操作</p></callout>'
            '<img src="image" mime="image/png" alt="说明图"/>'
            "<table><tr><th>名称</th><th>值</th></tr><tr><td>CPU</td><td>4</td></tr></table>"
            '<pre lang="Bash"><code>printf &#39;example&#39;<br/># &lt;literal&gt;</code></pre>'
            '<source token="file" name="example.html"/><p>'
            + html.escape(cls.long_text)
            + "</p>",
            "doc-b": "<title>第二页</title><p>短文。</p>",
        }

    def setUp(self):
        self.workspace = tempfile.TemporaryDirectory()
        self.addCleanup(self.workspace.cleanup)
        self.work = Path(self.workspace.name)
        self.source = self.work / "export"
        self.lark = FixtureLark(self.work, dict(self.files))
        export(
            self.lark,
            "space",
            self.source,
            pandoc=self.pandoc,
            source_origin="https://example.feishu.cn",
        )

    def review(self, page_ids):
        review = self.work / "review.json"
        review.write_text(
            json.dumps(
                {
                    "content_sha256": read_manifest(self.source)["content_sha256"],
                    "guide_url": "https://github.com/example/guides/blob/fixed-commit/skills/example-guide",
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

    def guide(self):
        guide = self.work / "maintained/example-guide"
        (guide / "references").mkdir(parents=True)
        (guide / "SKILL.md").write_text(
            '---\nname: example-guide\ndescription: A guide.\nmetadata:\n  version: "1.0.0"\n---\n\n'
            'An authored entry. [Pilot](references/pilot.md) [BBS](references/community.md)\n'
        )
        for name in ("pilot", "community"):
            (guide / f"references/{name}.md").write_text(f"Authored {name} advice.\n")
        seal(guide)
        return guide

    def public_export(self):
        export(self.lark, "space", self.source, pandoc=self.pandoc,
               source_origin="https://example.feishu.cn", replace=True, public_only=True)
        return read_manifest(self.source)

    def test_one_handbook_is_readable_by_bot_skill_and_site(self):
        guide = self.guide()
        before = check_skill(guide)
        manifest = self.public_export()
        review = self.review([p["page_id"] for p in manifest["pages"]])
        output = self.work / "published"
        build(self.source, review, output, guide=guide, version="1.1.0")
        compiled = output / "skills/example-guide"
        self.assertEqual(check_skill(guide), before)
        self.assertEqual(check_skill(compiled)["version"], "1.1.0")
        self.assertIn("An authored entry.", (compiled / "SKILL.md").read_text())
        self.assertEqual((compiled / "references/pilot.md").read_bytes(),
                         (guide / "references/pilot.md").read_bytes())
        self.assertEqual((compiled / "references/community.md").read_bytes(),
                         (guide / "references/community.md").read_bytes())
        corpus = compiled / "references"
        rows = json.loads((corpus / "manifest.json").read_text())["documents"]
        self.assertEqual(len(rows), 4)
        for row in rows:
            if row["doc_id"].startswith("doc-"):
                self.assertEqual((corpus / row["file"]).read_bytes(),
                                 (output / "site" / row["file"].removeprefix("handbook/")).read_bytes())
                self.assertEqual(row["revision"], 3)
            else:
                self.assertEqual((corpus / row["file"]).read_bytes(), (guide / "references" / row["file"]).read_bytes())
                self.assertIn("/blob/fixed-commit/", row["url"])
                self.assertEqual(row["revision"], "1.0.0")
            self.assertEqual(row["sharing"], "anyone_readable")
        self.assertEqual({r['doc_id'] for r in rows if r['doc_id'].startswith('example-guide:')},
                         {'example-guide:pilot.md', 'example-guide:community.md'})
        self.assertEqual(pack(compiled, self.work / "dist1")["sha256"],
                         pack(compiled, self.work / "dist2")["sha256"])
        # A later import removes retired generated pages without changing the
        # maintained entry or leaving an older answer in the bot's directory.
        self.lark.deleted = True
        self.lark.files["doc-a"] = "<title>Updated</title><p>Current rule.</p>"
        self.public_export()
        remaining = read_manifest(self.source)["pages"][0]["page_id"]
        build(self.source, self.review([remaining]), self.work / "next",
              guide=compiled, version="1.2.0")
        latest = self.work / "next/skills/example-guide"
        check_skill(latest)
        retired = next(r for r in rows if r["doc_id"] == "doc-b")
        self.assertFalse((latest / "references" / retired["file"]).exists())
        self.assertEqual((latest / "SKILL.md").read_text().count("references/handbook/index.md"), 1)

    def test_unverified_private_and_mid_export_permission_changes_stop_import(self):
        guide = self.guide()
        pages = read_manifest(self.source)["pages"]
        with self.assertRaisesRegex(ExportError, "public-only"):
            build(self.source, self.review([p["page_id"] for p in pages]),
                  self.work / "unverified", guide=guide, version="1.1.0")
        before = read_manifest(self.source)
        self.lark.files["doc-a"] += '<synced_reference src-token="linked" src-block-id="qa"/>'
        self.lark.files["linked:qa"] = "<fragment><p>Private QA</p></fragment>"

        def private_source(token):
            if token == "linked":
                raise ExportError("未公开")
            return "anyone_readable"

        with patch.object(self.lark, "public_sharing", side_effect=private_source):
            with self.assertRaisesRegex(ExportError, "未公开"):
                self.public_export()
        self.assertEqual(read_manifest(self.source), before)
        calls = {}

        def revoke(token):
            calls[token] = calls.get(token, 0) + 1
            if calls[token] > 1:
                raise ExportError("已撤回公开")
            return "anyone_readable"

        with patch.object(self.lark, "public_sharing", side_effect=revoke):
            with self.assertRaisesRegex(ExportError, "已撤回公开"):
                self.public_export()
        self.assertEqual(read_manifest(self.source), before)

    def test_guide_changes_during_build_and_version_reuse_are_rejected(self):
        guide = self.guide()
        manifest = self.public_export()
        review = self.review([p["page_id"] for p in manifest["pages"]])
        with self.assertRaisesRegex(ExportError, "新版本"):
            build(self.source, review, self.work / "same", guide=guide, version="1.0.0")
        copytree = shutil.copytree

        def copy_and_edit(*args, **kwargs):
            result = copytree(*args, **kwargs)
            (guide / "references/pilot.md").write_text("A concurrent edit")
            return result

        with patch("generate_skills.shutil.copytree", side_effect=copy_and_edit):
            with self.assertRaises(ExportError):
                build(self.source, review, self.work / "changed", guide=guide, version="1.1.0")
        self.assertFalse((self.work / "changed").exists())
        self.assertEqual((guide / "references/pilot.md").read_text(), "A concurrent edit")

    def test_images_tables_long_short_documents_and_links_survive(self):
        manifest = read_manifest(self.source)
        self.assertEqual(len(manifest["pages"]), 2)
        first, second = manifest["pages"]
        text = (self.source / "content" / first["path"]).read_text()
        self.assertIn(self.long_text, text)
        self.assertIn("# 第一页\n", text)
        self.assertIn("## 示例\n", text)
        self.assertIn("``` bash\nprintf 'example'\n# <literal>\n```", text)
        self.assertIn("> 重要操作", text)
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
            export(
                self.lark,
                "space",
                self.source,
                pandoc=self.pandoc,
                source_origin="https://example.feishu.cn",
                replace=True,
            )
        self.assertEqual((self.source / "manifest.json").read_bytes(), before)
        self.lark.drift = False
        page = self.source / "content" / pages[0]["path"]
        page.write_text("manual change")
        with self.assertRaises(ExportError):
            export(
                self.lark,
                "space",
                self.source,
                pandoc=self.pandoc,
                source_origin="https://example.feishu.cn",
                replace=True,
            )
        self.assertEqual(page.read_text(), "manual change")

    def test_rename_and_deletion_remove_stale_generated_pages(self):
        before = read_manifest(self.source)
        removed = before["pages"][1]["page_id"]
        self.lark.deleted = True
        self.lark.title = "改名后的标题"
        export(
            self.lark,
            "space",
            self.source,
            pandoc=self.pandoc,
            source_origin="https://example.feishu.cn",
            replace=True,
        )
        after = read_manifest(self.source)
        self.assertEqual(after["pages"][0]["page_id"], before["pages"][0]["page_id"])
        self.assertEqual(after["pages"][0]["title"], "改名后的标题")
        self.assertFalse((self.source / "content" / removed).exists())

    def test_unchanged_content_reuses_review_and_paths_cannot_overlap(self):
        manifest = read_manifest(self.source)
        review = self.review([page["page_id"] for page in manifest["pages"]])
        export(
            self.lark,
            "space",
            self.source,
            pandoc=self.pandoc,
            source_origin="https://example.feishu.cn",
            replace=True,
        )
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

    def test_unsupported_dynamic_blocks_cannot_be_published(self):
        with patch.object(
            self.lark,
            "document",
            return_value={"revision_id": 3, "content": "<title>Example</title><task/>"},
        ):
            export(
                self.lark,
                "space",
                self.source,
                pandoc=self.pandoc,
                source_origin="https://example.feishu.cn",
                replace=True,
            )
        manifest = read_manifest(self.source)
        self.assertTrue(all(page["warnings"] for page in manifest["pages"]))
        with self.assertRaisesRegex(ExportError, "转换警告"):
            build(
                self.source,
                self.review([page["page_id"] for page in manifest["pages"]]),
                self.work / "published",
            )

    def test_synced_content_revision_and_cycle(self):
        self.lark.files["doc-a"] += (
            '<synced_reference src-token="linked" src-block-id="block"/>'
        )
        self.lark.files["linked:block"] = (
            "<fragment><synced-source><h2>同步标题</h2><p>引用正文。</p></synced-source></fragment>"
        )
        export(
            self.lark,
            "space",
            self.source,
            pandoc=self.pandoc,
            source_origin="https://example.feishu.cn",
            replace=True,
        )
        before = read_manifest(self.source)
        page = before["pages"][0]
        self.assertIn(
            "### 同步标题", (self.source / "content" / page["path"]).read_text()
        )
        self.assertEqual(
            before["includes"],
            [{"document_token": "linked", "block_id": "block", "revision": 3}],
        )
        document = self.lark.document
        count = self.lark.calls["linked:block"]

        def edit_reference(token, block=None):
            value = document(token, block)
            if block and self.lark.calls["linked:block"] > count + 1:
                value["revision_id"] += 1
            return value

        with (
            patch.object(self.lark, "document", side_effect=edit_reference),
            self.assertRaisesRegex(ExportError, "同步块"),
        ):
            export(
                self.lark,
                "space",
                self.source,
                pandoc=self.pandoc,
                source_origin="https://example.feishu.cn",
                replace=True,
            )
        self.assertEqual(read_manifest(self.source), before)
        self.lark.files["linked:block"] = (
            '<synced_reference src-token="linked" src-block-id="block"/>'
        )
        with self.assertRaisesRegex(ExportError, "循环"):
            export(
                self.lark,
                "space",
                self.source,
                pandoc=self.pandoc,
                source_origin="https://example.feishu.cn",
                replace=True,
            )
        self.assertEqual(read_manifest(self.source), before)

    def test_image_crops_do_not_publish_hidden_pixels_or_share_wrong_variant(self):
        self.lark.files["doc-a"] += (
            '<img src="cropped" mime="image/png" crop="[0,0,0.5,1]"/>'
            '<img src="cropped" mime="image/png" crop="[0.5,0,1,1]"/>'
        )
        attachment = self.lark.attachment

        def download(token, destination, *, kind="media"):
            if token != "cropped":
                return attachment(token, destination, kind=kind)
            original = Image.new("RGB", (4, 2))
            original.putdata([(255, 0, 0), (0, 255, 0), (0, 0, 255), (0, 0, 0)] * 2)
            original.save(destination, format="PNG")

        with patch.object(self.lark, "attachment", side_effect=download):
            export(
                self.lark,
                "space",
                self.source,
                pandoc=self.pandoc,
                source_origin="https://example.feishu.cn",
                replace=True,
            )
            before = read_manifest(self.source)
            colors = []
            for file in (self.source / "content").rglob("*.png"):
                with Image.open(file) as image:
                    self.assertNotEqual(image.size, (4, 2))
                    if image.size == (2, 2):
                        colors.append(image.getpixel((0, 0)))
            self.assertCountEqual(colors, [(255, 0, 0), (0, 0, 255)])
            self.lark.files["doc-a"] += (
                '<img src="cropped" mime="image/png" crop="[0,0,-1,1]"/>'
            )
            with self.assertRaisesRegex(ExportError, "裁剪范围"):
                export(
                    self.lark,
                    "space",
                    self.source,
                    pandoc=self.pandoc,
                    source_origin="https://example.feishu.cn",
                    replace=True,
                )
            self.assertEqual(read_manifest(self.source), before)


if __name__ == "__main__":
    unittest.main()
