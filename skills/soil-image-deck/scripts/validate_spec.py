#!/usr/bin/env python3
import argparse
from pathlib import Path
import sys

try:
    import yaml
except ImportError:
    raise SystemExit("PyYAML is required: python -m pip install PyYAML")


ALLOWED_PHASES = {"hook", "attention", "action"}
ALLOWED_LAYOUTS = {
    "cover_hero", "question_focus", "misconception_dual", "comparison_split",
    "process_timeline", "classification_grid", "case_scene_analysis",
    "relationship_map", "data_focus", "summary_three", "action_next_step",
    "section_divider",
}


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--spec", required=True)
    args = parser.parse_args()
    path = Path(args.spec)
    data = yaml.safe_load(path.read_text(encoding="utf-8"))
    errors = []

    required_root = ("schema_version", "deck", "canvas", "soil_flow", "design_system", "layout_router", "slides", "validation")
    for key in required_root:
        if not isinstance(data, dict) or key not in data:
            errors.append(f"root: missing {key}")

    slides = data.get("slides", []) if isinstance(data, dict) else []
    pages = []
    for index, slide in enumerate(slides, 1):
        where = f"slides[{index}]"
        for key in ("page", "soil_phase", "role", "learning_task", "core_point", "semantic_structure", "layout", "visible_text", "speaker_only", "visual", "output"):
            if not isinstance(slide, dict) or key not in slide:
                errors.append(f"{where}: missing {key}")
        if not isinstance(slide, dict):
            continue
        pages.append(slide.get("page"))
        if slide.get("soil_phase") not in ALLOWED_PHASES:
            errors.append(f"{where}: invalid soil_phase")
        layout_id = (slide.get("layout") or {}).get("id") if isinstance(slide.get("layout"), dict) else None
        if layout_id and layout_id not in ALLOWED_LAYOUTS:
            errors.append(f"{where}: unsupported layout id {layout_id}")

    if not slides:
        errors.append("root: slides must be a non-empty list")
    if len(pages) != len(set(pages)):
        errors.append("slides: duplicate page numbers")
    if pages and pages != list(range(1, len(pages) + 1)):
        errors.append("slides: page numbers must be sequential from 1")

    expected = (data.get("deck") or {}).get("slide_count") if isinstance(data, dict) else None
    if expected is not None and expected != len(slides):
        errors.append(f"deck.slide_count={expected}, but slides has {len(slides)} entries")

    font_feel = (((data.get("design_system") or {}).get("typography") or {}).get("font_feel", ""))
    if not any(token in str(font_feel).lower() for token in ("圓", "round")):
        errors.append("design_system.typography.font_feel must require rounded typography")

    phases = {slide.get("soil_phase") for slide in slides if isinstance(slide, dict)}
    if slides and phases != ALLOWED_PHASES:
        errors.append("slides must include hook, attention, and action phases")

    if errors:
        print("INVALID")
        for error in errors:
            print(f"- {error}")
        return 1
    print(f"VALID: {path} ({len(slides)} SOIL slides)")
    return 0


if __name__ == "__main__":
    sys.exit(main())

