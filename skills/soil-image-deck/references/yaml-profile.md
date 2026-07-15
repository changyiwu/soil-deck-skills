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

`plate` 模式可在單頁加入選用的渲染區塊：

```yaml
plate:
  image: "page_01"
  image_box: {x: 0, y: 0, w: 13.333, h: 7.5, no_crop: false}
  blocks:
    - {type: title, source: visible_text.title, x: 0.75, y: 0.55, w: 11.8, h: 1.15}
```

若省略 `plate.blocks`，可攜式封裝器會依 `visible_text.title`、`subtitle`、`labels`、`items`、`bullets` 與 `body` 建立保守的預設文字框。需要精確版面時，明確提供 `plate.blocks`。

`design_system.typography` 可設定 `plate_font_fallback_policy: "warn_and_fallback"`（預設）與 `fallback_font_preferences`。找不到指定圓體時，封裝器只會在輸出記錄明確警告後使用該清單中已安裝的可讀繁中字型；設定 `strict` 則維持停止封裝。
