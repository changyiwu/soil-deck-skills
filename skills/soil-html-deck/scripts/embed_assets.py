#!/usr/bin/env python3
import argparse
import base64
import io
import mimetypes
from pathlib import Path
import re


def raw_data_uri(path: Path) -> str:
    mimetypes.add_type("font/ttf", ".ttf")
    mimetypes.add_type("font/woff2", ".woff2")
    mime = mimetypes.guess_type(path.name)[0] or "application/octet-stream"
    return f"data:{mime};base64," + base64.b64encode(path.read_bytes()).decode("ascii")


def asset_uri(path: Path, max_width: int, quality: int) -> str:
    if path.suffix.lower() not in {".png", ".jpg", ".jpeg", ".webp", ".gif"}:
        return raw_data_uri(path)
    try:
        from PIL import Image
    except ImportError:
        return raw_data_uri(path)

    with Image.open(path) as image:
        image = image.convert("RGB")
        if max_width and image.width > max_width:
            height = round(image.height * max_width / image.width)
            image = image.resize((max_width, height), Image.Resampling.LANCZOS)
        buffer = io.BytesIO()
        image.save(buffer, format="JPEG", quality=quality, optimize=True)
    return "data:image/jpeg;base64," + base64.b64encode(buffer.getvalue()).decode("ascii")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--template", required=True)
    parser.add_argument("--output", required=True)
    parser.add_argument("--asset", action="append", default=[], help="TOKEN=PATH")
    parser.add_argument("--text", action="append", default=[], help="TOKEN=PATH")
    parser.add_argument("--max-width", type=int, default=1600)
    parser.add_argument("--quality", type=int, default=82)
    args = parser.parse_args()

    template = Path(args.template)
    output = Path(args.output)
    html = template.read_text(encoding="utf-8")

    for item in args.asset:
        if "=" not in item:
            raise SystemExit(f"Invalid --asset value: {item}")
        token, raw_path = item.split("=", 1)
        path = Path(raw_path)
        if not path.is_file():
            raise SystemExit(f"Missing asset: {path}")
        placeholder = "{{ASSET_" + token + "}}"
        if placeholder not in html:
            raise SystemExit(f"Template does not contain {placeholder}")
        html = html.replace(placeholder, asset_uri(path, args.max_width, args.quality))

    for item in args.text:
        if "=" not in item:
            raise SystemExit(f"Invalid --text value: {item}")
        token, raw_path = item.split("=", 1)
        path = Path(raw_path)
        if not path.is_file():
            raise SystemExit(f"Missing text asset: {path}")
        placeholder = "{{TEXT_" + token + "}}"
        if placeholder not in html:
            raise SystemExit(f"Template does not contain {placeholder}")
        html = html.replace(placeholder, path.read_text(encoding="utf-8"))

    unresolved = sorted(set(re.findall(r"\{\{(?:ASSET|TEXT)_[A-Z0-9_]+\}\}", html)))
    if unresolved:
        raise SystemExit("Unresolved asset tokens: " + ", ".join(unresolved))

    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(html, encoding="utf-8")
    print(f"WROTE: {output} ({output.stat().st_size} bytes)")


if __name__ == "__main__":
    main()
