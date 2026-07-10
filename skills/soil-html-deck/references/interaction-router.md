# SOIL Interaction Router

Choose interaction from the learning relationship. Use `none` when interaction adds no explanatory value.

| Semantic structure | Preferred interactions | Controlled layout examples |
|---|---|---|
| `focus` | `none`, `reveal` | `cover_hero`, `question_focus` |
| `contrast` | `toggle_compare`, `sortable_table` | `comparison_split`, `misconception_dual` |
| `sequence` | `stepper`, `reveal` | `process_timeline` |
| `classification` | `filter_cards`, `tabs` | `classification_grid` |
| `causality` | `reveal`, `decision_tree` | `relationship_map` |
| `hierarchy` | `tabs`, `hotspot`, `reveal` | `relationship_map` |
| `scenario` | `tabs`, `decision_tree` | `case_scene_analysis` |
| `data` | `chart`, `slider`, `sortable_table` | `data_focus` |
| `decision` | `decision_tree`, `quiz` | `action_next_step` |
| `practice` | `quiz`, `drag_match`, `slider` | content-specific |
| `synthesis` | `reveal`, `tabs`, `none` | `summary_three`, `action_next_step` |

Each interaction block must specify:

- `type`: one allowed interaction.
- `goal`: the understanding or decision it supports.
- `trigger`: `click`, `input`, `drag`, or `auto_after_user_action`.
- `initial_state`: what is visible before interaction.
- `states` or `controls`: the finite behaviors available.
- `fallback`: complete static meaning when JS, motion, hover, or precision input is unavailable.

Avoid hover-only content, decorative counters, automatic motion before user intent, and multiple competing interactions on one page.
