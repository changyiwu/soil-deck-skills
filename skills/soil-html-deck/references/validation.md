# SOIL HTML Validation

Validate in this order:

1. YAML schema, page sequence, SOIL phases, rounded typography, layout IDs, semantic/interaction compatibility, and minimum meaningful interactions.
2. Golden trio: cover, standard content page, and representative interaction page.
3. Final HTML structure: exact slide count, sequential `data-slide`, declared `data-interaction`, live text, and no image-slideshow substitution.
4. Portability: every `<img>` is a data URI; strict-offline builds have no remote scripts, styles, fonts, or images.
5. Navigation: keyboard, visible controls, progress, phase label, page label, focus, and hash state.
6. Interaction: initial state, all controls, result feedback, reset/revisit behavior, and static fallback.
7. Responsive QA: common desktop viewport plus narrow viewport; no clipped titles, unreachable controls, or unreadable text.
8. Accessibility: semantic controls, alt text, focus-visible, `aria-live`, keyboard parity, and reduced motion.

Reject decorative interaction, hover-only teaching content, baked body text, relative final asset paths, undefined DOM globals, external dependencies in strict-offline mode, and interactions whose meaning disappears without animation.
