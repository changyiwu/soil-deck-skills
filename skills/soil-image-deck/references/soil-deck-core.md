# SOIL Deck Core

Use one renderer-neutral planning model for Image, PowerPoint, and HTML outputs.

Core fields cover audience, purpose, SOIL flow, design system, page role, learning task, core point, semantic structure, visible copy, speaker-only content, and visual intent. Keep renderer-specific coordinates and behaviors outside the core.

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
  visual: {brief: "Concrete visual intent"}
```

## Renderer mapping

| Core field | Image/PPTX | Interactive HTML |
|---|---|---|
| `visible_text` | baked or plate overlay | live DOM text |
| `visual` | full slide or plate | hero/supporting asset |
| `layout.id` | image composition | responsive component |
| `semantic_structure` | visual relationship | interaction routing |
| `speaker_only` | notes or talk track | optional speaker mode |

When upgrading an Image Deck to HTML, preserve the core and add HTML-only `interaction`, `accessibility`, responsive behavior, and static fallback fields. Do not restart concept planning unless the existing core is incomplete.
