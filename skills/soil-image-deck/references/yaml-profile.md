# SOIL YAML Profile

Use these top-level sections:

```yaml
schema_version: "soil_image_deck_v2"
deck: {}
canvas: {}
soil_flow: {}
design_system: {}
rhythm_policy: {}
layout_router: {}
slides: []
validation: {}
```

The fixed layer belongs in `design_system`; controlled layout choices belong in `layout_router`; page teaching data belongs in `slides`.

Required per-slide fields:

```yaml
- page: 1
  soil_phase: "hook"
  role: "cover"
  learning_task: "Know why this topic matters"
  core_point: "One teachable claim"
  semantic_structure: "focus"
  layout: {id: "cover_hero", variant: "left_title_right_visual"}
  visible_text: {title: "Short title"}
  speaker_only: "What the teacher explains aloud"
  visual: "Concrete image brief"
  output: "slides/images/page_01.png"
```

Use percentage zones for image prompts. Use PowerPoint coordinates only in `plate` overlay blocks.

