"""Resolve Lark resources and containers before Pandoc parses standard HTML."""

import hashlib
import html
import json
from html.parser import HTMLParser
from pathlib import Path
from typing import ClassVar
from urllib.parse import urlsplit

from .lark import ExportError, Lark
from .media import crop_bounds, crop_image


class NativeHTML(HTMLParser):
    STANDARD: ClassVar[frozenset[str]] = frozenset(
        [
            "p",
            "b",
            "strong",
            "i",
            "em",
            "u",
            "s",
            "del",
            "sub",
            "sup",
            "blockquote",
            "ul",
            "ol",
            "li",
            "code",
            "pre",
            "br",
            "hr",
            "table",
            "thead",
            "tbody",
            "tr",
            "td",
            "th",
            "caption",
            "colgroup",
            "col",
            "a",
            "span",
            "figure",
            "div",
        ]
    )
    IMAGES: ClassVar[dict[str, str]] = {
        "image/png": ".png",
        "image/jpeg": ".jpeg",
        "image/gif": ".gif",
        "image/webp": ".webp",
        "image/svg+xml": ".svg",
    }

    def __init__(
        self,
        page: Path,
        lark: Lark,
        include,
        source_origin: str | None,
        active=frozenset(),
    ):
        super().__init__()
        self.page, self.lark, self.include, self.active = page, lark, include, active
        self.source_origin = source_origin
        self.parts = []
        self.warnings = []
        self.downloads = {}
        self.images = 0

    @staticmethod
    def tag(tag: str) -> str:
        if tag == "title":
            return "h1"
        if len(tag) == 2 and tag[0] == "h" and tag[1] in "123456":
            return "h" + str(min(int(tag[1]) + 1, 6))
        if tag == "callout":
            return "blockquote"
        return tag

    def render(self, xml: str) -> str:
        self.feed(xml)
        self.close()
        return "".join(self.parts)

    def media(self, attrs: dict, *, image: bool, board: bool = False) -> str:
        token = attrs.get("token") or attrs.get("src")
        if not token:
            raise ExportError("文档素材缺少资源标识，未导出。")
        extension = ".png" if board else self.IMAGES.get(attrs.get("mime"))
        if image and not extension:
            raise ExportError("图片格式尚不支持，未导出。")
        bounds = crop_bounds(attrs.get("crop")) if image else None
        key = token
        if bounds:
            key += "\0" + json.dumps(bounds, separators=(",", ":"))
            extension = ".png"
        relative = (
            ("assets/" if image else "attachments/")
            + hashlib.sha256(key.encode()).hexdigest()
            + (extension if image else ".bin")
        )
        target = self.page.parent / relative
        if not target.exists():
            target.parent.mkdir(parents=True, exist_ok=True)
            self.lark.attachment(token, target, kind="whiteboard" if board else "media")
            if bounds:
                crop_image(target, bounds)
        return relative

    def handle_starttag(self, tag, attrs):
        values = dict(attrs)
        if tag in {"synced_reference", "synced-reference"}:
            key = (values.get("src-token"), values.get("src-block-id"))
            if not all(key) or key in self.active or len(self.active) >= 32:
                raise ExportError("同步块引用缺失或循环，未导出。")
            nested = NativeHTML(
                self.page,
                self.lark,
                self.include,
                self.source_origin,
                self.active | {key},
            )
            self.parts.append(nested.render(self.include(*key)))
            self.warnings.extend(nested.warnings)
            self.downloads.update(nested.downloads)
            self.images += nested.images
        elif tag in {"synced-source", "synced_source", "fragment"}:
            pass
        elif tag in {"img", "image", "whiteboard"}:
            path = self.media(values, image=True, board=tag == "whiteboard")
            self.parts.append(
                f'<img src="{path}" alt="{html.escape(values.get("alt", ""), quote=True)}">'
            )
            self.images += 1
        elif tag in {"source", "file"}:
            path = self.media(values, image=False)
            name = values.get("name") or "附件"
            self.downloads[path] = name
            self.parts.append(f'<a href="{path}">{html.escape(name)}</a>')
        elif tag == "cite" and values.get("file-type") in {"wiki", "docx", "doc"}:
            token, title = values.get("doc-id"), values.get("title")
            if not token or not title:
                raise ExportError("文档引用信息不完整，未导出。")
            url = values.get("href") or values.get("url")
            if not url:
                if self.source_origin is None:
                    raise ExportError(
                        "文档引用缺少原始网址，请用知识库完整网址重新导出。"
                    )
                url = self.source_origin + "/" + values["file-type"] + "/" + token
            if urlsplit(url).scheme not in {"https", "http"}:
                raise ExportError("文档引用的网址无效，未导出。")
            self.parts.append(
                f'<a href="{html.escape(url, quote=True)}">{html.escape(title)}</a>'
            )
        elif tag == "iframe":
            url = values.get("url", "")
            if urlsplit(url).scheme not in {"https", "http"}:
                raise ExportError("嵌入页面缺少有效链接，未导出。")
            self.parts.append(
                f'<a href="{html.escape(url, quote=True)}">打开原文中的外部页面</a>'
            )
        elif (
            tag in self.STANDARD
            or tag == "title"
            or tag == "callout"
            or tag in {f"h{i}" for i in range(1, 7)}
        ):
            attributes = ""
            if tag == "a":
                href = values.get("href", "")
                if urlsplit(href).scheme not in {"https", "http", "mailto", ""}:
                    raise ExportError("原文链接类型尚不支持，未导出。")
                attributes = f' href="{html.escape(href, quote=True)}"'
            if tag in {"td", "th"}:
                for name in ("rowspan", "colspan"):
                    if name in values:
                        attributes += (
                            f' {name}="{html.escape(values[name], quote=True)}"'
                        )
            if tag == "pre":
                language = values.get("lang", "").lower()
                if language and language != "plain text":
                    attributes = f' class="{html.escape(language, quote=True)}"'
                if values.get("caption", "").strip():
                    self.parts.append(
                        f"<p><em>{html.escape(values['caption'].strip())}</em></p>"
                    )
            self.parts.append(f"<{self.tag(tag)}{attributes}>")
        else:
            self.warnings.append(f"原文包含尚未支持的内容块：{tag}。")

    def handle_endtag(self, tag):
        if tag in {"br", "hr", "col"}:
            return
        if (
            tag in self.STANDARD
            or tag in {"title", "callout"}
            or tag in {f"h{i}" for i in range(1, 7)}
        ):
            self.parts.append(f"</{self.tag(tag)}>")

    def handle_data(self, data):
        self.parts.append(html.escape(data, quote=False))

    def handle_comment(self, data):
        if "unsupported" in data.lower():
            self.warnings.append("飞书未能读取原文中的部分内容块。")
