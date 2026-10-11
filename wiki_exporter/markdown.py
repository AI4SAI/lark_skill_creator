"""Pandoc owns document conversion; this module only resolves exported links."""

import hashlib
import html
import json
import os
import subprocess
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urlsplit

from .lark import ExportError, Lark


class Resources(HTMLParser):
    def __init__(self, content: str):
        super().__init__()
        self.attachments = []
        self.embedded = []
        self.images = []
        self.links = []
        self.unsupported = []
        self.feed(content)

    def handle_starttag(self, tag, attrs):
        values = dict(attrs)
        if tag in {"sheet", "bitable", "mindnote", "slides"} or (
            tag == "cite" and values.get("file-type") in {"sheets", "bitable"}
        ):
            self.embedded.append(tag)
        if tag in {
            "synced_reference",
            "synced_source",
            "source-synced",
            "base_ref",
            "task",
            "okr",
            "okr-objective",
            "okr-key-result",
        }:
            self.unsupported.append(tag)
        if tag in {"img", "image", "whiteboard"}:
            self.images.append(values.get("token") or len(self.images))
        if tag == "iframe":
            url = values.get("url", "")
            parsed = urlsplit(url)
            if parsed.scheme not in {"https", "http"} or not parsed.hostname:
                self.unsupported.append("iframe")
            else:
                self.links.append(url)
        if tag in {"source", "file"} and values.get("token"):
            self.attachments.append(values)

    def handle_comment(self, data):
        if "unsupported" in data.lower():
            self.unsupported.append(data.strip())


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
    value, current: Path, aliases: dict[str, Path], dependencies: set[str]
) -> None:
    if isinstance(value, list):
        for item in value:
            rewrite_links(item, current, aliases, dependencies)
    elif isinstance(value, dict):
        if value.get("t") == "Link":
            target = value["c"][-1]
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
            rewrite_links(child, current, aliases, dependencies)


def convert(
    document: Path,
    page: Path,
    xml: str,
    aliases: dict[str, Path],
    lark: Lark,
    pandoc: str,
) -> tuple[list[str], list[str]]:
    resources = Resources(xml)
    if resources.embedded:
        raise ExportError(
            "文档包含嵌入表格或思维笔记，需先在飞书中整理为可独立发布的内容。"
        )
    page.parent.mkdir(parents=True, exist_ok=True)
    ast = page.parent / "document.json"
    warnings = [
        pandoc_run(
            pandoc,
            [
                str(document),
                "--from=docx",
                "--to=json",
                "--extract-media=assets",
                "--output=document.json",
            ],
            page.parent,
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

    if images(tree) < len(resources.images):
        warnings.append("图片或画板数量少于飞书原文，请核对导出文件。")
    if resources.unsupported:
        warnings.append("飞书原文含未支持的内容块，请先核对原文。")
    dependencies: set[str] = set()
    rewrite_links(tree, page, aliases, dependencies)
    warnings.append(
        pandoc_run(
            pandoc,
            ["--from=json", "--to=gfm", "--wrap=none", "--output=index.md"],
            page.parent,
            json.dumps(tree),
        )
    )
    ast.unlink()
    if resources.links:
        with page.open("a", encoding="utf-8") as stream:
            stream.write(
                "\n\n"
                + "\n\n".join(
                    f'<a href="{html.escape(url, quote=True)}">打开原文中的外部页面</a>'
                    for url in dict.fromkeys(resources.links)
                )
                + "\n"
            )
    if resources.attachments:
        links = []
        attached = set()
        for item in resources.attachments:
            token = item["token"]
            if token in attached:
                continue
            attached.add(token)
            # Binary MIME plus the download filename avoids active HTML/JS attachments.
            filename = hashlib.sha256(token.encode()).hexdigest() + ".bin"
            target = page.parent / "attachments" / filename
            target.parent.mkdir(exist_ok=True)
            lark.attachment(token, target)
            label = html.escape(item.get("name") or "附件", quote=True)
            links.append(
                f'<a href="attachments/{filename}" download="{label}">{label}</a>'
            )
        with page.open("a", encoding="utf-8") as stream:
            stream.write("\n\n## 附件\n\n" + "\n\n".join(links) + "\n")
    return [message.strip() for message in warnings if message.strip()], sorted(
        dependencies
    )
