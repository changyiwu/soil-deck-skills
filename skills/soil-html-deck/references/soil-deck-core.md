# SOIL Deck Core

Use one renderer-neutral planning model for Image, PowerPoint, and HTML outputs.

## Required root sections

```yaml
schema_version: "soil_interactive_deck_v1"
deck: {}
canvas: {}
soil_flow: {}
design_system: {}
layout_router: {}
interaction_router: {}
slides: []
validation: {}
```

`design_system` owns the fixed visual shell. `layout_router` owns controlled page silhouettes. `interaction_router` maps semantic relationships to allowed behaviors. `slides` owns teaching data.

## Required slide fields

```yaml
- page: 1
  soil_phase: "hook"
  role: "cover"
  learning_task: "Know why the topic matters"
  core_point: "One teachable claim"
  semantic_structure: "focus"
  layout: {id: "cover_hero", variant: "left_title_right_visual"}
  visible_text: {title: "Short title"}
  speaker_only: "What the teacher explains aloud"
  visual: {mode: "baked", brief: "Concrete image brief"}
  interaction: {type: "none", goal: "", fallback: "Static cover"}
  accessibility: {keyboard: true, touch: true, reduced_motion: true}
```

## Renderer mapping

| Core field | Image/PPTX | Interactive HTML |
|---|---|---|
| `visible_text` | baked or plate overlay | live DOM text |
| `visual` | full slide or plate | hero/supporting asset |
| `layout.id` | image composition | responsive component |
| `semantic_structure` | visual relationship | interaction routing |
| `speaker_only` | notes or talk track | optional speaker mode |
| `interaction` | ignored/static fallback | live HTML/SVG/Canvas behavior |

Do not encode renderer-specific coordinates in the core. Store PowerPoint overlays or HTML breakpoints inside renderer-specific blocks only.
