#!/usr/bin/env python3
import argparse
from pathlib import Path
import sys

try:
    import yaml
except ImportError:
    raise SystemExit("PyYAML is required: python -m pip install PyYAML")


ALLOWED_PHASES = {"hook", "attention", "action"}
ALLOWED_OUTPUT_MODES = {"baked", "plate"}
ALLOWED_PLANNING_MODES = {"quick", "yaml_spec"}
ALLOWED_GENERATION_STRATEGIES = {"sequential", "subagents"}
ALLOWED_STYLE_LOCKS = {"none", "golden_sample"}
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

    if not isinstance(data, dict):
        print("INVALID")
        print("- root: YAML must be a mapping")
        return 1

    required_root = ("schema_version", "deck", "canvas", "soil_flow", "design_system", "layout_router", "slides", "validation")
    for key in required_root:
        if key not in data:
            errors.append(f"root: missing {key}")

    if data.get("schema_version") != "soil_image_deck_v2":
        errors.append("schema_version must be soil_image_deck_v2")

    deck = data.get("deck")
    if not isinstance(deck, dict):
        errors.append("deck must be a mapping")
        deck = {}
    enum_fields = {
        "output_mode": ALLOWED_OUTPUT_MODES,
        "planning_mode": ALLOWED_PLANNING_MODES,
        "generation_strategy": ALLOWED_GENERATION_STRATEGIES,
        "style_lock": ALLOWED_STYLE_LOCKS,
    }
    for field, allowed in enum_fields.items():
        if deck.get(field) not in allowed:
            errors.append(f"deck.{field} must be one of {sorted(allowed)}")

    canvas = data.get("canvas")
    if not isinstance(canvas, dict):
        errors.append("canvas must be a mapping")
        canvas = {}
    ratio = canvas.get("target_ratio")
    if not isinstance(ratio, str) or ":" not in ratio:
        errors.append("canvas.target_ratio must use W:H format")
    else:
        try:
            ratio_width, ratio_height = (float(part) for part in ratio.split(":", 1))
            if ratio_width <= 0 or ratio_height <= 0:
                raise ValueError
        except ValueError:
            errors.append("canvas.target_ratio must contain positive numbers")

    design_system = data.get("design_system")
    if not isinstance(design_system, dict):
        errors.append("design_system must be a mapping")
        design_system = {}

    slides = data.get("slides", [])
    if not isinstance(slides, list):
        errors.append("root: slides must be a list")
        slides = []
    pages = []
    outputs = []
    for index, slide in enumerate(slides, 1):
        where = f"slides[{index}]"
        for key in ("page", "soil_phase", "role", "learning_task", "core_point", "semantic_structure", "layout", "visible_text", "speaker_only", "visual", "output"):
            if not isinstance(slide, dict) or key not in slide:
                errors.append(f"{where}: missing {key}")
        if not isinstance(slide, dict):
            continue
        page = slide.get("page")
        if not isinstance(page, int) or isinstance(page, bool):
            errors.append(f"{where}: page must be an integer")
        else:
            pages.append(page)
        if slide.get("soil_phase") not in ALLOWED_PHASES:
            errors.append(f"{where}: invalid soil_phase")
        layout = slide.get("layout")
        layout_id = layout.get("id") if isinstance(layout, dict) else None
        if not layout_id:
            errors.append(f"{where}: layout.id is required")
        elif layout_id not in ALLOWED_LAYOUTS:
            errors.append(f"{where}: unsupported layout id {layout_id}")

        output = slide.get("output")
        if not isinstance(output, str) or not output.strip():
            errors.append(f"{where}: output must be a non-empty path")
        else:
            outputs.append(output)

        visible_text = slide.get("visible_text")
        if not isinstance(visible_text, dict):
            errors.append(f"{where}: visible_text must be a mapping")

        plate = slide.get("plate")
        if plate is not None:
            if not isinstance(plate, dict):
                errors.append(f"{where}: plate must be a mapping")
            else:
                blocks = plate.get("blocks", [])
                if not isinstance(blocks, list):
                    errors.append(f"{where}.plate.blocks must be a list")
                else:
                    for block_index, block in enumerate(blocks, 1):
                        block_where = f"{where}.plate.blocks[{block_index}]"
                        if not isinstance(block, dict):
                            errors.append(f"{block_where}: must be a mapping")
                            continue
                        if not block.get("text") and not block.get("source"):
                            errors.append(f"{block_where}: text or source is required")
                        for coordinate in ("x", "y", "w", "h"):
                            if coordinate not in block:
                                errors.append(f"{block_where}: missing {coordinate}")

    if not slides:
        errors.append("root: slides must be a non-empty list")
    if len(pages) != len(set(pages)):
        errors.append("slides: duplicate page numbers")
    if len(outputs) != len(set(outputs)):
        errors.append("slides: duplicate output paths")
    if pages and pages != list(range(1, len(pages) + 1)):
        errors.append("slides: page numbers must be sequential from 1")

    expected = deck.get("slide_count")
    if expected is not None and expected != len(slides):
        errors.append(f"deck.slide_count={expected}, but slides has {len(slides)} entries")

    typography = design_system.get("typography")
    if not isinstance(typography, dict):
        errors.append("design_system.typography must be a mapping")
        typography = {}
    font_feel = typography.get("font_feel", "")
    if not any(token in str(font_feel).lower() for token in ("圓", "round")):
        errors.append("design_system.typography.font_feel must require rounded typography")
    fallback_policy = typography.get("plate_font_fallback_policy", "warn_and_fallback")
    if fallback_policy not in {"warn_and_fallback", "strict"}:
        errors.append("design_system.typography.plate_font_fallback_policy must be warn_and_fallback or strict")
    fallback_fonts = typography.get("fallback_font_preferences", [])
    if fallback_fonts and not isinstance(fallback_fonts, (str, list)):
        errors.append("design_system.typography.fallback_font_preferences must be a string or list")

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
