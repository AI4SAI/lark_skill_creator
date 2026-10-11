"""Preserve the visible part of a cropped native document image."""

import json
import math
from pathlib import Path

from PIL import Image, ImageOps

from .lark import ExportError


def crop_bounds(value: str | None) -> tuple[float, float, float, float] | None:
    if value is None:
        return None
    try:
        bounds = json.loads(value)
        if (
            not isinstance(bounds, list)
            or len(bounds) != 4
            or any(type(x) not in (int, float) or not math.isfinite(x) for x in bounds)
        ):
            raise ValueError
        left, top, right, bottom = (float(x) for x in bounds)
        if not (0 <= left < right <= 1 and 0 <= top < bottom <= 1):
            raise ValueError
    except (TypeError, ValueError) as error:
        raise ExportError("图片裁剪范围无效，未导出。") from error
    if (left, top, right, bottom) == (0, 0, 1, 1):
        return None
    return left, top, right, bottom


def crop_image(path: Path, bounds: tuple[float, float, float, float]) -> None:
    try:
        with Image.open(path) as original:
            if getattr(original, "n_frames", 1) > 1:
                raise ExportError("暂不支持动态图裁剪，未导出。")
            visible = ImageOps.exif_transpose(original)
            left, top, right, bottom = bounds
            box = (
                int(left * visible.width),
                int(top * visible.height),
                int(right * visible.width),
                int(bottom * visible.height),
            )
            if box[0] == box[2] or box[1] == box[3]:
                raise ExportError("图片裁剪后没有可见像素，未导出。")
            cropped = visible.crop(box)
        # PNG keeps the selected pixels without retaining the hidden source edges.
        cropped.save(path, format="PNG")
    except (OSError, ValueError, Image.DecompressionBombError) as error:
        raise ExportError("无法保留图片的裁剪范围，未导出。") from error
