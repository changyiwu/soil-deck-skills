# SOIL HTML Patterns

## Page shell

Use full-viewport slide sections with a progress bar, SOIL phase label, page number, explicit navigation controls, and a centered safe-area container.

```html
<main id="deck">
  <section class="slide active" data-slide="1" data-section="引起動機" data-interaction="none">...</section>
</main>
```

Avoid a fixed 1920×1080 canvas scaled with transforms. Use CSS grid/flex, `clamp()`, aspect ratios, and breakpoint-specific reflow. On narrow screens, allow the active page to scroll vertically rather than shrinking text below readability.

## Design system

Map YAML tokens to CSS custom properties:

```css
:root {
  --bg: #f5f1e8;
  --primary: #176b87;
  --accent: #f4a261;
  --ink: #173042;
  --title-size: clamp(2.1rem, 5vw, 4.6rem);
}
```

Do not force one global theme. Preserve the requested palette, material, rounded typography, title anchor, card language, and recurring motif.

## Controlled components

- `cover_hero`: hero asset plus live CTA/navigation.
- `question_focus`: one question and optional progressive reveal.
- `comparison_split`: two live panels with toggle or sortable evidence.
- `process_timeline`: clickable stepper with current-step explanation.
- `classification_grid`: filterable or selectable cards.
- `relationship_map`: HTML nodes plus SVG connector layer.
- `case_scene_analysis`: supporting image plus tabbed interpretation.
- `data_focus`: SVG/Canvas/chart with declared controls and text summary.
- `summary_three`: three selectable takeaways.
- `action_next_step`: decision or CTA with visible result.

## Navigation

Support ArrowRight, Space, PageDown, ArrowLeft, PageUp, Home, End, and `F` for fullscreen. Provide visible previous/next buttons. Do not trigger slide navigation when a control, link, table header, form input, or interactive card is used.

Update progress, section label, page number, focus target, and URL hash on every page change. Bind explicit DOM references; do not depend on browser-generated globals from element IDs.

## Accessibility and motion

- Use semantic buttons and focus-visible styles.
- Add an `aria-live="polite"` status region for page and interaction results.
- Ensure every pointer interaction has keyboard activation.
- Never hide essential content behind hover.
- Implement `@media (prefers-reduced-motion: reduce)`.
- Give images useful alt text, or empty alt text when decorative.

## Asset policy

Use AI-generated or user-provided images as hero or supporting assets. Keep exact copy, formulas, tables, diagrams, and interaction labels live. Embed final images as data URIs for a portable single file.
