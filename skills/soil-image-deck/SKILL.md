---
name: soil-image-deck
description: Create SOIL-style image-first teaching presentations in which every slide is driven by an AI-generated full-page visual. Use when the user asks for a SOIL image deck, pure-image teaching slides, NotebookLM-style educational slides, a YAML-driven SOIL deck, visual-impact teacher training slides, or a baked/plate PPTX that follows 引起動機、維持注意、喚起行動 and the SOIL six-engine workflow.
---

# SOIL Image Deck

Use SOIL teaching decisions to create a coherent image-first deck. Produce a page plan and YAML design contract before image generation, lock the style with a golden sample, then generate, inspect, and package the deck.

## Configuration Axes

- `output_mode`: `baked` or `plate`.
- `planning_mode`: `quick` or `yaml_spec`.
- `generation_strategy`: `sequential` or `subagents`.
- `style_lock`: `none` or `golden_sample`.

Default to `yaml_spec`, `sequential`, and `golden_sample`. Use `subagents` only when the user explicitly requests parallel generation and the environment permits it.

## Hard Image Rule

- Generate every slide visual with Codex built-in image generation first.
- Do not replace image generation with Pillow, CSS, SVG, procedural shapes, or placeholders.
- Use an API/CLI image path only when the user explicitly requests it.
- Save every accepted image inside the project before packaging.

## Rounded Typography Policy

Default to bold rounded Traditional Chinese display lettering: thick even strokes, soft terminals, generous counters, friendly proportions, and low corner sharpness.

For `baked`, repeat the rounded typography requirement in every image prompt. Prohibit angular geometric Chinese type, condensed mechanical type, sharp wedges, and techno-stencil forms.

For `plate`, use the first installed font from `jf open 粉圓 2.1`, `GenSenRounded TW`, or `GenJyuuGothic`. If none is installed, stop before packaging and report the missing rounded Chinese font. Never silently fall back to an angular default.

## SOIL Six-Engine Workflow

1. **Concept positioning**: one big idea, three sub-ideas, misunderstandings, takeaway, minimal fact pack, and slide-vs-talk split.
2. **Context positioning**: arrange 引起動機 → 維持注意 → 喚起行動. A 10-slide default rhythm is approximately 2 / 6 / 2.
3. **Page architecture**: give each page one role, one core point, one learning task, one semantic relationship, one `layout.id`, minimal visible text, and one visual brief.
4. **Cognitive editing**: check 降雜訊、區塊化、增資訊、結構化、順脈絡、步驟化.
5. **Style construction**: create `spec.yaml` from `assets/soil-spec-template.yaml`; define palette, fixed shell, rounded typography, layout router, safe area, image policy, and validation rules.
6. **Production**: validate YAML, approve a golden sample, generate images, inspect the montage, selectively regenerate failed pages, package the PPTX, render it again, and verify delivery.

When the user supplies an existing validated SOIL YAML spec, skip engines 1–5 only if its concept, flow, page roles, and visual system are already explicit.

## Production Commands

Validate YAML:

```powershell
python .\scripts\validate_spec.py --spec .\spec.yaml
```

Verify generated images:

```powershell
python .\scripts\verify_images.py --spec .\spec.yaml --images-dir .\slides\images
```

In Codex, package with the Presentations skill and Artifact Tool. Embed one full-bleed image per slide, render the exported PPTX, inspect the montage, and run overflow checks.

For environments without Artifact Tool, `scripts/pack_pptx.py` is a portability fallback. It center-crops baked images to 16:9 and refuses silent substitution when no rounded Chinese font is available for `plate` mode.

## Output Modes

- `baked`: the generated image contains the short visible text. Best for demos, social sharing, openings, and visual storytelling.
- `plate`: generate a text-free designed plate with reserved text zones; overlay editable text afterward. Best for long-lived teaching decks, revisions, formulas, and exact data.

Keep formulas, precise geometry, charts, and numeric evidence native/editable when correctness matters.

## References

- Read `references/soil-engines.md` for required planning outputs.
- Read `references/yaml-profile.md` before writing `spec.yaml`.
- Read `references/layout-recipes.md` before assigning layouts.
- Read `references/prompting.md` before image generation.
- Read `references/subagent-batching.md` when the user requests parallel generation.
- Read `references/validation.md` before packaging and delivery.

