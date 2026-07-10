# SOIL Deck Validation

Validate teaching quality and artifact quality.

Teaching checks:

- The deck follows 引起動機 → 維持注意 → 喚起行動.
- Every page has one learning task and one core point.
- The layout exposes the intended relationship.
- Oral-only explanations are not crammed into the image.

Image checks:

- Exact text is correct and no extra text appears.
- Chinese display type is visibly bold and rounded, not angular or condensed.
- Safe area, subject count, layout, palette, material, and golden-sample style pass.
- No screen mockup, logo, watermark, or accidental UI appears.

Delivery checks:

1. Validate YAML and image count/ratio.
2. Inspect every source image and a montage.
3. Package the deck.
4. Render the exported PPTX and inspect the rendered montage.
5. Run overflow checks and report final absolute paths.

