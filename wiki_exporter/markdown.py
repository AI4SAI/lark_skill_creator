"""Pandoc owns document conversion; this module only resolves exported links."""

import html
import json
import os
import subprocess
from pathlib import Path
from urllib.parse import urlsplit

from .lark import ExportError, Lark
from .native_html import NativeHTML


def pandoc_run(
    pandoc: str, args: list[str], cwd: Path, content: str | None = None
) -> str:
    result = subprocess.run(
        [pandoc, *args],
        cwd=cwd,
        input=content,
        text=True,
        capture_output=True,
        timeout=120,
        check=False,
    )
    if result.returncode:
        raise ExportError(f"Pandoc 转换失败，退出码 {result.returncode}。")
    # Diagnostics are retained for editorial review, never silently discarded.
    return result.stderr


def rewrite_links(
    value,
    current: Path,
    aliases: dict[str, Path],
    dependencies: set[str],
    downloads: dict[str, str],
) -> None:
    if isinstance(value, list):
        for item in value:
            rewrite_links(item, current, aliases, dependencies, downloads)
    elif isinstance(value, dict):
        if value.get("t") == "Link":
            target = value["c"][-1]
            if target[0] in downloads:
                name = html.escape(downloads[target[0]], quote=True)
                value["t"], value["c"] = (
                    "RawInline",
                    ["html", f'<a href="{target[0]}" download="{name}">{name}</a>'],
                )
                return
            url = urlsplit(target[0])
            parts = url.path.rstrip("/").split("/")
            if (
                url.scheme == "https"
                and url.hostname
                and url.hostname.endswith((".feishu.cn", ".larksuite.com"))
                and not url.fragment
                and len(parts) >= 3
                and parts[-2] in {"wiki", "docx", "doc"}
                and parts[-1] in aliases
            ):
                destination = aliases[parts[-1]]
                target[0] = Path(
                    os.path.relpath(destination, current.parent)
                ).as_posix()
                dependencies.add(destination.parent.name)
        for child in value.values():
            rewrite_links(child, current, aliases, dependencies, downloads)


def convert(
    page: Path,
    xml: str,
    aliases: dict[str, Path],
    lark: Lark,
    pandoc: str,
    include,
    source_origin: str | None,
    source_page_url: str | None = None,
) -> tuple[list[str], list[str]]:
    resources = NativeHTML(page, lark, include, source_origin, source_page_url=source_page_url)
    content = resources.render(xml)
    page.parent.mkdir(parents=True, exist_ok=True)
    ast = page.parent / "document.json"
    warnings = [
        pandoc_run(
            pandoc,
            [
                "--from=html+tex_math_single_backslash",
                "--to=json",
                "--output=document.json",
            ],
            page.parent,
            content,
        )
    ]
    tree = json.loads(ast.read_text(encoding="utf-8"))

    def images(value):
        if isinstance(value, list):
            return sum(images(child) for child in value)
        if isinstance(value, dict):
            return int(value.get("t") == "Image") + sum(
                images(child) for child in value.values()
            )
        return 0

    if images(tree) != resources.images:
        warnings.append("图片或画板数量少于飞书原文，请核对导出文件。")
    warnings.extend(resources.warnings)
    dependencies: set[str] = set()
    rewrite_links(tree, page, aliases, dependencies, resources.downloads)
    warnings.append(
        pandoc_run(
            pandoc,
            ["--from=json", "--to=gfm", "--wrap=none", "--output=index.md"],
            page.parent,
            json.dumps(tree),
        )
    )
    ast.unlink()
    return [message.strip() for message in warnings if message.strip()], sorted(
        dependencies
    )
