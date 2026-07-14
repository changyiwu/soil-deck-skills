# SOIL 簡報核心

圖片、PowerPoint 與 HTML 輸出共用一套與渲染器無關的規劃模型。

核心欄位涵蓋受眾、目的、SOIL 流程、設計系統、頁面角色、學習任務、核心重點、語意結構、可見文字、僅供講者使用的內容，以及視覺意圖。渲染器專屬的座標與行為須放在核心之外。

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

## 渲染器對應

| 核心欄位 | 圖片／PPTX | 互動 HTML |
|---|---|---|
| `visible_text` | baked 圖片文字或 plate 疊字 | 即時 DOM 文字 |
| `visual` | 滿版投影片或底板 | 主視覺／輔助素材 |
| `layout.id` | 圖片構圖 | 響應式元件 |
| `semantic_structure` | 視覺關係 | 互動路由 |
| `speaker_only` | 備忘稿或講述內容 | 選用的講者模式 |

將 Image Deck 升級為 HTML 時，保留核心內容，並加入 HTML 專屬的 `interaction`、`accessibility`、響應式行為與靜態備援欄位。除非現有核心不完整，否則不需重新進行概念規劃。
