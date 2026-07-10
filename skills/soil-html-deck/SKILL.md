---
name: soil-html-deck
description: Create YAML-driven SOIL interactive HTML presentations as portable single-file web decks. Use when the user asks for an HTML deck, interactive slides, a web presentation, a SOIL Image Deck upgraded with interaction, clickable teaching diagrams, responsive presentation pages, sortable tables, charts, decision trees, steppers, quizzes, or a presentation that should preserve SOIL visual rules while adding native HTML/CSS/JS behavior.
---

# SOIL Interactive HTML Deck

Create an HTML deck as the interactive superset of SOIL Image Deck. Share the same SOIL teaching flow, page architecture, design system, controlled layout router, image briefs, and YAML core. Render live text and interaction with HTML/CSS/JS instead of turning the deck into an image slideshow.

## Output Contract

- Produce one browser-openable `.html` file with inline CSS and JS.
- Embed accepted images as `data:image/...;base64,...` for a portable final file.
- Keep titles, paragraphs, labels, cards, tables, formulas, charts, decision nodes, and controls as live HTML, SVG, Canvas, or math markup.
- Permit baked text only on intentional cover, section-divider, or closing hero images.
- Use built-in image generation for AI visual assets. Do not replace requested AI visuals with procedural placeholders.
- Preserve keyboard, mouse, and touch navigation; include reduced-motion behavior and a no-interaction fallback.

## Shared SOIL Core

Start from the renderer-neutral fields in `references/soil-deck-core.md`. Extend them with HTML interaction and accessibility fields from `assets/interactive-spec-template.yaml`.

Use these configuration axes:

- `planning_mode`: `quick` or `yaml_spec`; default `yaml_spec`.
- `visual_mode`: `native`, `asset`, `plate`, or hero-only `baked`.
- `interaction_level`: `none`, `guided`, or `exploratory`; default `guided`.
- `portability`: `single_file` or `linked`; default `single_file`.
- `style_lock`: `none` or `golden_trio`; default `golden_trio`.

## Workflow

1. **Concept and flow**: define one big idea, audience outcome, misconceptions, and 引起動機 → 維持注意 → 喚起行動.
2. **Page architecture**: assign one teaching job, core point, learning task, semantic structure, controlled layout, and short visible copy per page.
3. **YAML contract**: create `spec.yaml` from `assets/interactive-spec-template.yaml`; lock design, responsive behavior, interaction, accessibility, and validation before authoring HTML.
4. **Interaction routing**: select interaction from meaning, not decoration. Read `references/interaction-router.md`.
5. **Golden trio**: approve a cover, a standard content page, and one representative interaction page before building the full deck.
6. **Asset production**: generate only the required images. Prefer text-free plates and supporting assets for live HTML pages.
7. **HTML production**: use the component and navigation patterns in `references/html-patterns.md`; keep the selected theme instead of forcing a fixed dark-tech style.
8. **Verification**: validate YAML, embed assets, run the standalone verifier, inspect every page in a browser, and test desktop plus narrow viewport behavior.

When a validated SOIL Image Deck YAML already exists, migrate its renderer-neutral fields rather than restarting planning. Add `learning_task`, `speaker_only`, `interaction`, `accessibility`, and responsive layout behavior, then validate the upgraded spec.

## Interaction Policy

- Use interaction only when it clarifies comparison, sequence, classification, causality, hierarchy, data, decision, practice, or exploration.
- Default to two to four meaningful interactions per 8–12 page deck; more is acceptable only when the learning design requires it.
- Keep one primary interaction per slide.
- Every interaction needs an explicit learning goal, initial state, keyboard/touch controls, and static fallback.
- Do not hide essential teaching content behind hover-only behavior.
- Do not use motion as decoration; support `prefers-reduced-motion`.

## Typography and Visual Rules

Use the YAML design system. Default Chinese display type remains bold, rounded, friendly, and low-angular. Prefer `jf open 粉圓 2.1`, `GenSenRounded TW`, or `GenJyuuGothic` when locally available; use a declared rounded web-font or a documented system fallback for portable HTML.

Maintain a fixed shell and controlled variation: title anchor, palette, material language, recurring motif, safe area, and progress chrome stay consistent while layout and interaction respond to content.

## Commands

Validate the interactive YAML:

```powershell
python .\scripts\validate_interactive_spec.py --spec .\spec.yaml
```

Embed generated assets into a final HTML file:

```powershell
python .\scripts\embed_assets.py --template .\slides.template.html --output .\slides.html --asset COVER=.\assets\cover.png
```

Verify the final standalone deck:

```powershell
python .\scripts\verify_html.py --html .\slides.html --spec .\spec.yaml --strict-offline
```

## References

- Read `references/soil-deck-core.md` before migrating or authoring YAML.
- Read `references/interaction-router.md` before assigning interactions.
- Read `references/html-patterns.md` before implementing HTML.
- Read `references/validation.md` before delivery.
