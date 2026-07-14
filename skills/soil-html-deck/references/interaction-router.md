# SOIL 互動路由

依學習關係選擇互動。若互動無法增加解釋價值，使用 `none`。

| 語意結構 | 建議互動 | 受控版型範例 |
|---|---|---|
| `focus` | `none`、`reveal` | `cover_hero`、`question_focus` |
| `contrast` | `toggle_compare`、`sortable_table` | `comparison_split`、`misconception_dual` |
| `sequence` | `stepper`、`reveal` | `process_timeline` |
| `classification` | `filter_cards`、`tabs` | `classification_grid` |
| `causality` | `reveal`、`decision_tree` | `relationship_map` |
| `hierarchy` | `tabs`、`hotspot`、`reveal` | `relationship_map` |
| `scenario` | `tabs`、`decision_tree` | `case_scene_analysis` |
| `data` | `chart`、`slider`、`sortable_table` | `data_focus` |
| `decision` | `decision_tree`、`quiz` | `action_next_step` |
| `practice` | `quiz`、`drag_match`、`slider` | 依內容決定 |
| `synthesis` | `reveal`、`tabs`、`none` | `summary_three`、`action_next_step` |

每個互動區塊都必須指定：

- `type`：一種允許的互動。
- `goal`：互動支援的理解或決策。
- `trigger`：`click`、`input`、`drag` 或 `auto_after_user_action`。
- `initial_state`：互動前可見的內容。
- `states` 或 `controls`：可用的有限行為。
- `fallback`：當 JS、動態效果、滑鼠懸停或精細輸入不可用時，仍能完整表達意義的靜態備援。

避免只能用滑鼠懸停觸發的內容、裝飾性計數器、使用者表達意圖前自動播放的動態效果，以及同一頁內互相競爭的多個互動。
