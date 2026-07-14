# SOIL 簡報核心

圖片、PowerPoint 與 HTML 輸出共用一套與渲染器無關的規劃模型。

## 必要的根層區段

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

`design_system` 管理固定視覺框架；`layout_router` 管理受控的頁面輪廓；`interaction_router` 將語意關係對應至允許的行為；`slides` 管理教學資料。

## 必要的投影片欄位

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

## 渲染器對應

| 核心欄位 | 圖片／PPTX | 互動 HTML |
|---|---|---|
| `visible_text` | baked 圖片文字或 plate 疊字 | 即時 DOM 文字 |
| `visual` | 滿版投影片或底板 | 主視覺／輔助素材 |
| `layout.id` | 圖片構圖 | 響應式元件 |
| `semantic_structure` | 視覺關係 | 互動路由 |
| `speaker_only` | 備忘稿或講述內容 | 選用的講者模式 |
| `interaction` | 忽略／靜態備援 | 即時 HTML／SVG／Canvas 行為 |

不得在核心中編寫渲染器專屬座標。PowerPoint 疊字或 HTML 中斷點只能存放在渲染器專屬區塊內。
