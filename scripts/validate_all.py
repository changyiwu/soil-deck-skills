#!/usr/bin/env python3
import argparse
import ast
import re
import subprocess
import sys
import tempfile
from pathlib import Path

import yaml
from PIL import Image
from pptx import Presentation


ROOT = Path(__file__).resolve().parents[1]
SKILLS = {
    "image": ROOT / "skills" / "soil-image-deck",
    "teaching": ROOT / "skills" / "soil-teaching-deck",
    "html": ROOT / "skills" / "soil-html-deck",
}


def run(*parts: str) -> None:
    command = [sys.executable, *map(str, parts)]
    print("RUN:", " ".join(command))
    subprocess.run(command, cwd=ROOT, check=True)


def run_expect_failure(*parts: str) -> None:
    command = [sys.executable, *map(str, parts)]
    print("RUN (expect failure):", " ".join(command))
    result = subprocess.run(command, cwd=ROOT, check=False)
    if result.returncode == 0:
        raise SystemExit("Expected validation failure, but command succeeded")


def validate_python() -> None:
    files = sorted((ROOT / "skills").rglob("*.py")) + sorted((ROOT / "scripts").rglob("*.py"))
    for path in files:
        ast.parse(path.read_text(encoding="utf-8"), filename=str(path))
    print(f"VALID: Python AST ({len(files)} files)")


def validate_markdown() -> None:
    errors = []
    portable_files = [ROOT / "README.md", *sorted((ROOT / "skills").rglob("*.md"))]
    forbidden = re.compile(r"(?:(?<![A-Za-z])[A-Za-z]:[\\/]|/home/|/mnt/|/sessions/|~/\.claude/)")
    link_pattern = re.compile(r"\[[^\]]+\]\(([^)#]+)(?:#[^)]+)?\)")
    for path in [ROOT / "AGENTS.md", *portable_files]:
        text = path.read_text(encoding="utf-8")
        fences = sum(1 for line in text.splitlines() if line.strip().startswith("```"))
        if fences % 2:
            errors.append(f"{path.relative_to(ROOT)}: unbalanced code fences")
        if path in portable_files and forbidden.search(text):
            errors.append(f"{path.relative_to(ROOT)}: contains a machine-specific path")
        for target in link_pattern.findall(text):
            if re.match(r"^(?:https?://|mailto:|obsidian:)", target):
                continue
            resolved = (path.parent / target).resolve()
            if not resolved.exists():
                errors.append(f"{path.relative_to(ROOT)}: missing link target {target}")
    if errors:
        raise SystemExit("INVALID MARKDOWN\n- " + "\n- ".join(errors))
    print("VALID: Markdown fences, portable paths, and local links")


def validate_skill(skill_dir: Path) -> None:
    path = skill_dir / "SKILL.md"
    text = path.read_text(encoding="utf-8")
    parts = text.split("---", 2)
    if len(parts) != 3 or parts[0].strip():
        raise SystemExit(f"{path}: invalid YAML frontmatter")
    metadata = yaml.safe_load(parts[1])
    if not isinstance(metadata, dict) or set(metadata) != {"name", "description"}:
        raise SystemExit(f"{path}: frontmatter must contain only name and description")
    if metadata["name"] != skill_dir.name:
        raise SystemExit(f"{path}: name must match folder")
    if not str(metadata["description"]).strip():
        raise SystemExit(f"{path}: description is required")
    line_count = len(text.splitlines())
    if line_count > 500:
        raise SystemExit(f"{path}: {line_count} lines exceeds the 500-line skill limit")

    agent_path = skill_dir / "agents" / "openai.yaml"
    agent = yaml.safe_load(agent_path.read_text(encoding="utf-8"))
    interface = (agent or {}).get("interface") or {}
    for key in ("display_name", "short_description", "default_prompt"):
        if not interface.get(key):
            raise SystemExit(f"{agent_path}: missing interface.{key}")
    if f"${skill_dir.name}" not in interface["default_prompt"]:
        raise SystemExit(f"{agent_path}: default_prompt must mention ${skill_dir.name}")

    references = set(re.findall(r"references/[A-Za-z0-9._/-]+\.md", text))
    for reference in references:
        if not (skill_dir / reference).is_file():
            raise SystemExit(f"{path}: missing referenced file {reference}")
    print(f"VALID SKILL: {skill_dir.name} ({line_count} lines, {len(references)} references)")


def validate_shared_core() -> None:
    image_core = (SKILLS["image"] / "references" / "soil-deck-core.md").read_text(encoding="utf-8")
    html_core = (SKILLS["html"] / "references" / "soil-deck-core.md").read_text(encoding="utf-8")
    if image_core.replace("\r\n", "\n") != html_core.replace("\r\n", "\n"):
        raise SystemExit("Shared soil-deck-core.md files have drifted")
    print("VALID: shared SOIL core files match")


def validate_image() -> None:
    skill = SKILLS["image"]
    spec = skill / "assets" / "soil-spec-template.yaml"
    run(skill / "scripts" / "validate_spec.py", "--spec", spec)
    run(skill / "scripts" / "pack_pptx.py", "--mode", "plate", "--spec", spec, "--check-spec")

    with tempfile.TemporaryDirectory(prefix="soil-image-smoke-") as raw_tmp:
        tmp = Path(raw_tmp)
        invalid_spec = tmp / "invalid-spec.yaml"
        invalid_data = yaml.safe_load(spec.read_text(encoding="utf-8"))
        invalid_data["schema_version"] = "unsupported"
        invalid_spec.write_text(yaml.safe_dump(invalid_data, allow_unicode=True, sort_keys=False), encoding="utf-8")
        run_expect_failure(skill / "scripts" / "validate_spec.py", "--spec", invalid_spec)
        images = tmp / "images"
        images.mkdir()
        for page in range(1, 4):
            Image.new("RGB", (1600, 900), (30 * page, 80, 120)).save(images / f"page_{page:02}.png")
        run(skill / "scripts" / "verify_images.py", "--spec", spec, "--images-dir", images)
        output = tmp / "smoke.pptx"
        run(skill / "scripts" / "pack_pptx.py", "--mode", "baked", "--images-dir", images, "--output", output)
        if not output.is_file() or len(Presentation(output).slides) != 3:
            raise SystemExit("Image Deck PPTX smoke test failed")
    print("VALID: Image Deck smoke tests")


def validate_html() -> None:
    skill = SKILLS["html"]
    spec = skill / "assets" / "interactive-spec-template.yaml"
    run(skill / "scripts" / "validate_interactive_spec.py", "--spec", spec)

    with tempfile.TemporaryDirectory(prefix="soil-html-smoke-") as raw_tmp:
        tmp = Path(raw_tmp)
        image_path = tmp / "cover.png"
        Image.new("RGBA", (64, 36), (20, 80, 120, 128)).save(image_path)
        template = tmp / "slides.template.html"
        output = tmp / "slides.html"
        template.write_text("""<!doctype html>
<html><head><meta content='width=device-width,initial-scale=1' name='viewport'>
<style>@media (prefers-reduced-motion: reduce){*{animation:none}}</style></head>
<body><div id='progress'></div><div id='section-tag'></div><div id='page-info'></div>
<div aria-live='polite'></div><main id='deck'>
<section class='slide active' data-slide='1' data-interaction='none'><img alt='' src='{{ASSET_COVER}}'></section>
<section class='slide' data-slide='2' data-interaction='toggle_compare'><button type='button'>比較</button></section>
<section class='slide' data-slide='3' data-interaction='decision_tree'><div role='button' tabindex='0'>選擇</div></section>
</main><script>document.addEventListener('keydown',()=>{});</script></body></html>""", encoding="utf-8")
        run(skill / "scripts" / "embed_assets.py", "--template", template, "--output", output, "--asset", f"COVER={image_path}")
        run(skill / "scripts" / "verify_html.py", "--html", output, "--spec", spec, "--strict-offline")
        if "data:image/png;base64," not in output.read_text(encoding="utf-8"):
            raise SystemExit("Transparent PNG was not preserved by embed_assets.py")
        external = tmp / "external.html"
        external.write_text(
            output.read_text(encoding="utf-8").replace("</head>", "<script src='app.js'></script></head>"),
            encoding="utf-8",
        )
        run_expect_failure(skill / "scripts" / "verify_html.py", "--html", external, "--spec", spec, "--strict-offline")
    print("VALID: HTML Deck smoke tests")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--target", choices=("all", "image", "teaching", "html"), default="all")
    args = parser.parse_args()

    validate_python()
    validate_markdown()
    selected = SKILLS if args.target == "all" else {args.target: SKILLS[args.target]}
    for skill in selected.values():
        validate_skill(skill)
    if args.target in {"all", "image", "html"}:
        validate_shared_core()
    if args.target in {"all", "image"}:
        validate_image()
    if args.target in {"all", "html"}:
        validate_html()
    print(f"ALL VALIDATIONS PASSED: {args.target}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
