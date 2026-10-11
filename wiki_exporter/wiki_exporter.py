"""Export Wiki documents using native Lark export and Pandoc."""

import argparse
import hashlib
import json
import re
import shutil
import sys
from datetime import datetime, timezone
from pathlib import Path

from .bundle import build_directory, canonical_directory, write_manifest
from .lark import ExportError, Lark
from .markdown import convert


def catalog(lark: Lark, space: str) -> list[dict]:
    records, seen, parents = [], set(), [""]
    while parents:
        parent = parents.pop()
        for node in lark.nodes(space, parent):
            token = node.get("node_token")
            if not isinstance(token, str) or not re.fullmatch(r"[A-Za-z0-9_-]+", token):
                raise ExportError("知识库节点标识缺失或无效。")
            if token in seen:
                raise ExportError("知识库目录出现重复节点。")
            seen.add(token)
            if not isinstance(node.get("title"), str) or not node.get("obj_token"):
                raise ExportError("知识库节点信息不完整。")
            records.append(
                {
                    **node,
                    "parent_node_token": parent,
                    "page_id": hashlib.sha256(token.encode()).hexdigest()[:24],
                }
            )
            if node.get("has_child"):
                parents.append(token)
    return records


def export(
    lark: Lark,
    space: str,
    output: Path,
    *,
    pandoc: str,
    selected: set[str] | None = None,
    replace: bool = False,
) -> dict:
    nodes = catalog(lark, space)
    known = {n["page_id"] for n in nodes}
    if selected and not selected <= known:
        raise ExportError("选中的文档已不存在于当前知识库，请重新核对目录。")
    chosen = [n for n in nodes if selected is None or n["page_id"] in selected]
    if not chosen:
        raise ExportError("没有选中可导出的文档。")
    if any(n["obj_type"] != "docx" for n in chosen):
        raise ExportError(
            "选中内容包含非 Docx 文档，请先用 --catalog 查看目录并选择需要发布的文档。"
        )
    with build_directory(
        output, replace=replace, kind="lark-wiki-export/v1"
    ) as staging:
        aliases = {
            token: staging / "content" / n["page_id"] / "index.md"
            for n in chosen
            for token in (n["node_token"], n["obj_token"])
        }
        records = []
        for node in chosen:
            token, page_id = node["obj_token"], node["page_id"]
            before = lark.document(token)
            original = staging / "originals" / page_id
            original.mkdir(parents=True)
            native = original / "source.docx"
            (original / "source.xml").write_text(before["content"], encoding="utf-8")
            exported_revision = lark.export_docx(token, native, before["revision_id"])
            if exported_revision != before["revision_id"]:
                raise ExportError(
                    "续查完成的是旧版本导出，未替换原输出；请重新执行以导出当前版本。"
                )
            page = aliases[node["node_token"]]
            warnings, dependencies = convert(
                native, page, before["content"], aliases, lark, pandoc
            )
            after = lark.document(token)
            if (
                before["revision_id"] != after["revision_id"]
                or before["content"] != after["content"]
            ):
                raise ExportError(
                    "导出期间文档被修改，本次输出未发布。请在编辑完成后重新导出。"
                )
            records.append(
                {
                    "page_id": page_id,
                    "node_token": node["node_token"],
                    "document_token": token,
                    "parent_node_token": node["parent_node_token"],
                    "title": node["title"],
                    "revision": before["revision_id"],
                    "path": str(page.relative_to(staging / "content")),
                    "warnings": warnings,
                    "dependencies": dependencies,
                }
            )
        current = catalog(lark, space)

        def topology(values):
            return {
                (
                    n["node_token"],
                    n["obj_token"],
                    n["obj_type"],
                    n["title"],
                    n["parent_node_token"],
                )
                for n in values
            }

        if topology(current) != topology(nodes):
            raise ExportError("导出期间知识库目录发生变化，本次输出未发布。")
        write_manifest(
            staging,
            {
                "kind": "lark-wiki-export/v1",
                "space_id": space,
                "exported_at": datetime.now(timezone.utc).isoformat(),
                "pages": records,
                "selection": sorted(selected) if selected is not None else "all",
            },
        )
    return {
        "output": str(output),
        "pages": len(records),
        "complete": True,
        "publication": "requires editorial review",
    }


def main() -> int:
    parser = argparse.ArgumentParser(
        description="导出飞书文档供审核，不自动发布网站或 Skill。"
    )
    parser.add_argument("space_id")
    parser.add_argument("--catalog", action="store_true", help="只列目录与稳定文档标识")
    parser.add_argument("--page-id", action="append", help="只导出所选文档，可重复")
    parser.add_argument("--output", type=Path, default=Path("wiki_export/current"))
    parser.add_argument(
        "--replace", action="store_true", help="更新未被手工修改的生成目录"
    )
    parser.add_argument("--pandoc", default="pandoc")
    args = parser.parse_args()
    lark = Lark(Path.cwd())
    try:
        if args.catalog:
            result = [
                {k: n[k] for k in ("page_id", "title", "obj_type", "parent_node_token")}
                for n in catalog(lark, args.space_id)
            ]
        else:
            if not shutil.which(args.pandoc):
                raise ExportError(
                    "未找到 Pandoc，请先安装，或通过 --pandoc 指定程序路径。"
                )
            output = canonical_directory(args.output)
            if not output.is_relative_to(Path.cwd()) or output == Path.cwd():
                raise ExportError("输出目录须位于当前工作目录内，不能是工作目录本身。")
            result = export(
                lark,
                args.space_id,
                output,
                pandoc=args.pandoc,
                selected=set(args.page_id) if args.page_id else None,
                replace=args.replace,
            )
        print(json.dumps(result, ensure_ascii=False, indent=2))
        return 0
    except (ExportError, OSError, ValueError) as error:
        print(
            json.dumps({"complete": False, "error": str(error)}, ensure_ascii=False),
            file=sys.stderr,
        )
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
