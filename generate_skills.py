"""Build site content and compact Skills from the same reviewed Markdown files."""

import argparse
import hashlib
import html
import json
import re
import shutil
import sys
from pathlib import Path
from urllib.parse import quote, urlsplit

from skill_package import check as check_skill, seal as seal_skill
from wiki_exporter.bundle import (
    build_directory,
    canonical_directory,
    read_manifest,
    review_digest,
    write_manifest,
)
from wiki_exporter.lark import ExportError


def build(source: Path, review: Path, output: Path, *, replace: bool = False,
          guide: Path | None = None, version: str | None = None) -> dict:
    source, output = canonical_directory(source), canonical_directory(output)
    if source.is_relative_to(output) or output.is_relative_to(source):
        raise ExportError("输入文档与输出目录不能重叠。")
    manifest = read_manifest(source)
    review_bytes = review.read_bytes()
    approved = json.loads(review_bytes)
    if manifest.get("kind") != "lark-wiki-export/v1":
        raise ExportError("输入不是当前导出工具生成的文档包。")
    digest = hashlib.sha256((source / "manifest.json").read_bytes()).hexdigest()
    if approved.get("content_sha256") != review_digest(manifest):
        raise ExportError("审核记录与当前导出版本不一致，请先复核本次变更。")
    pages = {p["page_id"]: p for p in manifest["pages"]}
    if len(pages) != len(manifest["pages"]):
        raise ExportError("导出清单包含重复文档。")
    selections = approved.get("skills")
    if not isinstance(selections, list) or not selections:
        raise ExportError("审核记录未指定需要发布的 Skill。")
    guide_manifest = None
    if guide is not None:
        guide = canonical_directory(guide)
        if guide.is_relative_to(output) or output.is_relative_to(guide):
            raise ExportError("维护中的 Skill 与生成目录不能重叠。")
        guide_manifest = check_skill(guide)
        guide_url = approved.get("guide_url", "").rstrip("/")
        url = urlsplit(guide_url)
        if url.scheme != "https" or not url.hostname or url.username or url.password or url.query or url.fragment:
            raise ExportError("审核记录需要 guide_url，指向本次简短参考的公开 Git 固定版本。")
        if len(selections) != 1 or selections[0]["name"] != guide_manifest["name"]:
            raise ExportError("统一资料包只接受已有的同名 Skill。")
        if not version or version == guide_manifest["version"] or not re.fullmatch(
            r"[0-9]+\.[0-9]+\.[0-9]+(?:-[a-z0-9.]+)?", version
        ):
            raise ExportError("请用 --version 为加入手册后的包指定新版本。")
        tokens = {p["document_token"] for p in manifest["pages"]} | {
            p["document_token"] for p in manifest.get("includes", [])
        }
        sharing = manifest.get("public_sharing", {})
        if not manifest.get("source_origin") or any(
            sharing.get(token) not in {"anyone_readable", "anyone_editable"} for token in tokens
        ):
            raise ExportError("统一资料包需要 --public-only 导出的公开正文及同步源。")
    elif version is not None:
        raise ExportError("--version 与 --guide 一起使用。")
    approved_pages = {page for item in selections for page in item["pages"]}
    with build_directory(output, replace=replace, kind="reviewed-docs/v1") as staging:
        published, names = set(), set()
        navigation = []
        for item in selections:
            name, description = item["name"], item["description"]
            if not re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", name) or name in names:
                raise ExportError("Skill 名称无效或重复。")
            if len(name) > 64:
                raise ExportError("Skill 名称不能超过 64 个字符。")
            names.add(name)
            if not isinstance(description, str) or not 1 <= len(description) <= 1024:
                raise ExportError("Skill 描述须为 1 至 1024 个字符。")
            selected = item["pages"]
            if (
                not isinstance(selected, list)
                or not selected
                or len(set(selected)) != len(selected)
            ):
                raise ExportError("Skill 文档选择为空或重复。")
            if not set(selected) <= pages.keys():
                raise ExportError("审核记录包含不存在的文档。")
            required, pending = set(), list(selected)
            while pending:
                page_id = pending.pop()
                if page_id in required:
                    continue
                if page_id not in approved_pages or page_id not in pages:
                    raise ExportError("文档引用了尚未审核的页面，未发布。")
                required.add(page_id)
                pending.extend(pages[page_id]["dependencies"])
            skill = staging / "skills" / name
            if guide is None:
                skill.mkdir(parents=True)
                references = skill / "references"
            else:
                shutil.copytree(guide, skill)
                references = skill / "references" / "handbook"
                # Only the new candidate's generated subtree is replaced.
                # The source guide and its other ten references remain intact.
                if references.exists():
                    shutil.rmtree(references)
                references.mkdir(parents=True)
            links = []
            documents = []
            for page_id in [*selected, *sorted(required.difference(selected))]:
                page = pages[page_id]
                if page["warnings"]:
                    raise ExportError(
                        "所选文档存在转换警告，需在原文中修正后重新导出。"
                    )
                relative = Path(page["path"])
                if (
                    relative.is_absolute()
                    or ".." in relative.parts
                    or relative != Path(page_id) / "index.md"
                ):
                    raise ExportError("文档路径无效。")
                source_dir = source / "content" / page_id
                target = references / page_id
                target.parent.mkdir(exist_ok=True)
                shutil.copytree(source_dir, target)
                title = html.escape(page["title"])
                if page_id in selected:
                    links.append(f"- [{title}](references/{page_id}/index.md)")
                if guide is not None:
                    text = (target / "index.md").read_text(encoding="utf-8")
                    documents.append({
                        "doc_id": page["document_token"], "title": page["title"],
                        "url": manifest["source_origin"] + "/wiki/" + page["node_token"],
                        "revision": page["revision"], "sharing": sharing[page["document_token"]],
                        "status": "fetched", "file": "handbook/" + page["path"], "characters": len(text),
                        "sha256": hashlib.sha256((target / "index.md").read_bytes()).hexdigest(),
                    })
                if page_id not in published:
                    dest = staging / "site" / page_id
                    dest.parent.mkdir(exist_ok=True)
                    shutil.copytree(source_dir, dest)
                    navigation.append({"title": page["title"], "path": page["path"]})
                    published.add(page_id)
            if guide is None:
                (skill / "SKILL.md").write_text(
                    "---\nname: " + json.dumps(name)
                    + "\ndescription: " + json.dumps(description, ensure_ascii=False)
                    + "\n---\n\n# " + item.get("title", name)
                    + "\n\n按需读取以下资料：\n\n" + "\n".join(links) + "\n",
                    encoding="utf-8",
                )
            else:
                # This is the existing bot reader's format, at the same path
                # that native Skill clients read. No second corpus is built.
                index = "# 手册原文\n\n" + "\n".join(
                    f'- [{html.escape(doc["title"])}]({doc["file"].removeprefix("handbook/")}) · [飞书原文]({doc["url"]}) · 修订 {doc["revision"]}'
                    for doc in documents
                ) + "\n"
                (references / "index.md").write_text(index, encoding="utf-8")
                for path in sorted((skill / "references").rglob("*.md")):
                    if path.is_relative_to(references):
                        continue
                    relative = path.relative_to(skill / "references").as_posix()
                    text = path.read_text(encoding="utf-8")
                    title = re.search(r"^# (.+)$", text, re.MULTILINE)
                    documents.append({
                        "doc_id": name + ":" + relative,
                        "title": title[1] if title else path.stem,
                        "url": guide_url + "/references/" + quote(relative),
                        "revision": guide_manifest["version"], "sharing": "anyone_readable",
                        "status": "fetched", "file": relative, "characters": len(text),
                        "sha256": hashlib.sha256(path.read_bytes()).hexdigest(),
                    })
                (skill / "references/manifest.json").write_text(json.dumps({
                    "fetched_at": manifest["exported_at"],
                    "source": "Published SAI guide and handbook", "documents": documents,
                    "includes": manifest.get("includes", []),
                }, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
                entry = (skill / "SKILL.md").read_text(encoding="utf-8").replace(
                    f'  version: "{guide_manifest["version"]}"', f'  version: "{version}"', 1
                )
                if "references/handbook/index.md" not in entry:
                    entry += "\n查具体操作、示例或 QA 时，按需读取[手册原文](references/handbook/index.md)。\n"
                (skill / "SKILL.md").write_text(entry, encoding="utf-8")
                seal_skill(skill)
        if read_manifest(source) != manifest:
            raise ExportError("构建期间输入文档发生变化，未发布。")
        if review.read_bytes() != review_bytes:
            raise ExportError("构建期间审核记录发生变化，未发布。")
        if guide is not None and check_skill(guide) != guide_manifest:
            raise ExportError("构建期间维护中的 Skill 发生变化，未发布。")
        write_manifest(
            staging,
            {
                "kind": "reviewed-docs/v1",
                "source_manifest_sha256": digest,
                "review_sha256": hashlib.sha256(review_bytes).hexdigest(),
                "navigation": navigation,
                "skills": sorted(names),
            },
        )
    return {"output": str(output), "pages": len(published), "skills": sorted(names)}


def main() -> int:
    parser = argparse.ArgumentParser(
        description="从审核通过的文档生成网站内容和 Skill。"
    )
    parser.add_argument("--source", type=Path, required=True)
    parser.add_argument("--review", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--replace", action="store_true")
    parser.add_argument("--guide", type=Path, help="保留已有 Skill 入口，加入同一份公开手册")
    parser.add_argument("--version", help="加入手册后的 Skill 版本")
    args = parser.parse_args()
    try:
        result = build(args.source, args.review, args.output, replace=args.replace,
                       guide=args.guide, version=args.version)
        print(json.dumps(result, ensure_ascii=False, indent=2))
        return 0
    except (ExportError, OSError, ValueError, KeyError, TypeError) as error:
        print(
            json.dumps({"complete": False, "error": str(error)}, ensure_ascii=False),
            file=sys.stderr,
        )
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
