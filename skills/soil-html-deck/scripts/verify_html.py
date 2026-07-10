#!/usr/bin/env python3
import argparse
from html.parser import HTMLParser
from pathlib import Path
import re
import sys

try:
    import yaml
except ImportError:
    raise SystemExit("PyYAML is required: python -m pip install PyYAML")


class DeckParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.slides = []
        self.images = []
        self.ids = []
        self.links = []
        self._current_slide = None

    def handle_starttag(self, tag, attrs):
        attr = dict(attrs)
        if "id" in attr:
            self.ids.append(attr["id"])
        if tag == "section" and "slide" in attr.get("class", "").split():
            self._current_slide = {
                "page": attr.get("data-slide"),
                "interaction": attr.get("data-interaction"),
                "buttons": 0,
            }
            self.slides.append(self._current_slide)
        if tag == "button" and self._current_slide:
            self._current_slide["buttons"] += 1
        if tag == "img":
            self.images.append(attr.get("src", ""))
        for key in ("src", "href"):
            if key in attr:
                self.links.append((tag, key, attr[key]))

    def handle_endtag(self, tag):
        if tag == "section":
            self._current_slide = None


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--html", required=True)
    parser.add_argument("--spec", required=True)
    parser.add_argument("--strict-offline", action="store_true")
    args = parser.parse_args()

    html_path, spec_path = Path(args.html), Path(args.spec)
    html = html_path.read_text(encoding="utf-8")
    spec = yaml.safe_load(spec_path.read_text(encoding="utf-8"))
    parsed = DeckParser()
    parsed.feed(html)
    errors = []

    expected = (spec.get("deck") or {}).get("slide_count")
    if len(parsed.slides) != expected:
        errors.append(f"slide count={len(parsed.slides)}, expected {expected}")

    actual_pages = [slide.get("page") for slide in parsed.slides]
    expected_pages = [str(i) for i in range(1, expected + 1)]
    if actual_pages != expected_pages:
        errors.append("data-slide values must be sequential from 1")

    planned = {
        str(slide["page"]): (slide.get("interaction") or {}).get("type", "none")
        for slide in spec.get("slides", [])
    }
    for slide in parsed.slides:
        page = slide.get("page")
        expected_type = planned.get(page)
        if slide.get("interaction") != expected_type:
            errors.append(
                f"slide {page}: data-interaction={slide.get('interaction')}, expected {expected_type}"
            )
        if expected_type != "none" and slide.get("buttons", 0) == 0:
            errors.append(f"slide {page}: interactive slide has no button controls")

    for index, src in enumerate(parsed.images, 1):
        if not src.startswith("data:image/"):
            errors.append(f"image {index}: src must be a data:image URI")

    if len(parsed.ids) != len(set(parsed.ids)):
        errors.append("HTML contains duplicate ids")

    if args.strict_offline:
        for tag, key, value in parsed.links:
            if value.startswith(("http://", "https://", "//", "file://")):
                errors.append(f"strict offline: external {tag} {key}={value[:80]}")
        if re.search(r"url\(\s*['\"]?https?://", html, re.IGNORECASE):
            errors.append("strict offline: external CSS url()")

    required_tokens = {
        "viewport meta": 'name="viewport"',
        "progress": 'id="progress"',
        "section label": 'id="section-tag"',
        "page label": 'id="page-info"',
        "aria live": 'aria-live="polite"',
        "keyboard navigation": "keydown",
        "reduced motion": "prefers-reduced-motion",
    }
    for label, token in required_tokens.items():
        if token not in html:
            errors.append(f"missing {label}")

    if errors:
        print("INVALID")
        for error in errors:
            print(f"- {error}")
        return 1
    print(
        f"VALID: {html_path} ({len(parsed.slides)} slides, "
        f"{len(parsed.images)} embedded images, strict_offline={args.strict_offline})"
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
