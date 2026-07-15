#!/usr/bin/env python3
import argparse
from pathlib import Path
import sys

try:
    import yaml
except ImportError:
    raise SystemExit("PyYAML is required: python -m pip install PyYAML")


PHASES = {"hook", "attention", "action"}
LAYOUTS = {
    "cover_hero", "question_focus", "misconception_dual", "comparison_split",
    "process_timeline", "classification_grid", "case_scene_analysis",
    "relationship_map", "data_focus", "summary_three", "action_next_step",
    "section_divider",
}
INTERACTIONS = {
    "none", "reveal", "toggle_compare", "stepper", "filter_cards", "tabs",
    "decision_tree", "sortable_table", "chart", "hotspot", "slider", "quiz",
    "drag_match",
}
ROUTER = {
    "focus": {"none", "reveal"},
    "contrast": {"none", "toggle_compare", "sortable_table", "reveal"},
    "sequence": {"none", "stepper", "reveal"},
    "classification": {"none", "filter_cards", "tabs"},
    "causality": {"none", "reveal", "decision_tree"},
    "hierarchy": {"none", "tabs", "hotspot", "reveal"},
    "scenario": {"none", "tabs", "decision_tree", "reveal"},
    "data": {"none", "chart", "slider", "sortable_table"},
    "decision": {"none", "decision_tree", "quiz"},
    "practice": {"none", "quiz", "drag_match", "slider"},
    "synthesis": {"none", "reveal", "tabs", "decision_tree"},
}
HERO_ROLES = {"cover", "section", "section_divider", "closing"}


def fail(errors, warnings):
    print("INVALID")
    for error in errors:
        print(f"- {error}")
    for warning in warnings:
        print(f"! {warning}")
    return 1


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--spec", required=True)
    args = parser.parse_args()
    path = Path(args.spec)
    data = yaml.safe_load(path.read_text(encoding="utf-8"))
    errors, warnings = [], []

    if not isinstance(data, dict):
        return fail(["root: YAML must be a mapping"], warnings)

    required_root = (
        "schema_version", "deck", "canvas", "soil_flow", "design_system",
        "layout_router", "interaction_router", "slides", "validation",
    )
    for key in required_root:
        if key not in data:
            errors.append(f"root: missing {key}")

    if data.get("schema_version") != "soil_interactive_deck_v1":
        errors.append("schema_version must be soil_interactive_deck_v1")

    sections = {}
    for key in ("deck", "canvas", "soil_flow", "design_system", "layout_router", "interaction_router", "validation"):
        value = data.get(key)
        if not isinstance(value, dict):
            errors.append(f"{key} must be a mapping")
            value = {}
        sections[key] = value

    deck = sections["deck"]
    if deck.get("portability") not in {"single_file", "linked"}:
        errors.append("deck.portability must be single_file or linked")
    ratio = sections["canvas"].get("target_ratio")
    if not isinstance(ratio, str) or ":" not in ratio:
        errors.append("canvas.target_ratio must use W:H format")
    else:
        try:
            ratio_width, ratio_height = (float(part) for part in ratio.split(":", 1))
            if ratio_width <= 0 or ratio_height <= 0:
                raise ValueError
        except ValueError:
            errors.append("canvas.target_ratio must contain positive numbers")

    slides = data.get("slides")
    if not isinstance(slides, list) or not slides:
        return fail(errors + ["slides must be a non-empty list"], warnings)

    pages, interactive_count = [], 0
    for index, slide in enumerate(slides, 1):
        where = f"slides[{index}]"
        if not isinstance(slide, dict):
            errors.append(f"{where}: must be a mapping")
            continue
        required = (
            "page", "soil_phase", "role", "learning_task", "core_point",
            "semantic_structure", "layout", "visible_text", "speaker_only",
            "visual", "interaction", "accessibility",
        )
        for key in required:
            if key not in slide:
                errors.append(f"{where}: missing {key}")

        page = slide.get("page")
        if not isinstance(page, int) or isinstance(page, bool):
            errors.append(f"{where}: page must be an integer")
        else:
            pages.append(page)
        if slide.get("soil_phase") not in PHASES:
            errors.append(f"{where}: invalid soil_phase")

        layout = slide.get("layout") or {}
        layout_id = layout.get("id") if isinstance(layout, dict) else None
        if layout_id not in LAYOUTS:
            errors.append(f"{where}: unsupported layout id {layout_id}")

        interaction = slide.get("interaction") or {}
        interaction_type = interaction.get("type") if isinstance(interaction, dict) else None
        if interaction_type not in INTERACTIONS:
            errors.append(f"{where}: unsupported interaction type {interaction_type}")
        elif interaction_type != "none":
            interactive_count += 1
            for key in ("goal", "trigger", "initial_state", "fallback"):
                if not interaction.get(key):
                    errors.append(f"{where}.interaction: missing {key}")

        semantic = slide.get("semantic_structure")
        allowed = ROUTER.get(semantic)
        if not allowed:
            errors.append(f"{where}: unsupported semantic_structure {semantic}")
        elif interaction_type not in allowed:
            errors.append(
                f"{where}: interaction {interaction_type} is not allowed for {semantic}"
            )

        visual = slide.get("visual") or {}
        visual_mode = visual.get("mode") if isinstance(visual, dict) else None
        if visual_mode not in {"native", "asset", "plate", "baked"}:
            errors.append(f"{where}: invalid visual.mode {visual_mode}")
        if visual_mode == "baked" and slide.get("role") not in HERO_ROLES:
            errors.append(f"{where}: baked visual is only allowed for hero roles")

        accessibility = slide.get("accessibility") or {}
        for key in ("keyboard", "touch", "reduced_motion"):
            if accessibility.get(key) is not True:
                errors.append(f"{where}.accessibility.{key} must be true")

    if len(pages) != len(set(pages)):
        errors.append("slides: duplicate page numbers")
    if pages != list(range(1, len(slides) + 1)):
        errors.append("slides: page numbers must be sequential from 1")

    expected = deck.get("slide_count")
    if expected != len(slides):
        errors.append(f"deck.slide_count={expected}, but slides has {len(slides)} entries")

    phases = {s.get("soil_phase") for s in slides if isinstance(s, dict)}
    if phases != PHASES:
        errors.append("slides must include hook, attention, and action phases")

    min_interactive = sections["interaction_router"].get("min_interactive_slides", 0)
    if not isinstance(min_interactive, int) or min_interactive < 0:
        errors.append("interaction_router.min_interactive_slides must be a non-negative integer")
        min_interactive = 0
    if interactive_count < min_interactive:
        errors.append(
            f"interactive slides={interactive_count}, below required minimum {min_interactive}"
        )

    typography = sections["design_system"].get("typography")
    if not isinstance(typography, dict):
        errors.append("design_system.typography must be a mapping")
        typography = {}
    font_feel = typography.get("font_feel", "")
    if not any(token in str(font_feel).lower() for token in ("圓", "round")):
        errors.append("design_system.typography.font_feel must require rounded typography")

    if errors:
        return fail(errors, warnings)
    print(f"VALID: {path} ({len(slides)} slides, {interactive_count} interactive)")
    for warning in warnings:
        print(f"! {warning}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
