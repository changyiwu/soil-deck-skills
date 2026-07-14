# SOIL YAML 規格

使用下列頂層區段：

```yaml
schema_version: "soil_image_deck_v2"
deck: {}
canvas: {}
soil_flow: {}
design_system: {}
rhythm_policy: {}
layout_router: {}
slides: []
validation: {}
```

固定層歸入 `design_system`；受控版型選擇歸入 `layout_router`；各頁教學資料歸入 `slides`。

每張投影片的必要欄位：

```yaml
- page: 1
  soil_phase: "hook"
  role: "cover"
  learning_task: "Know why this topic matters"
  core_point: "One teachable claim"
  semantic_structure: "focus"
  layout: {id: "cover_hero", variant: "left_title_right_visual"}
  visible_text: {title: "Short title"}
  speaker_only: "What the teacher explains aloud"
  visual: "Concrete image brief"
  output: "slides/images/page_01.png"
```

圖片提示詞使用百分比區域。只有 `plate` 疊字區塊能使用 PowerPoint 座標。
