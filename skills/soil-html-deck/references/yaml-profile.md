# SOIL 互動 HTML YAML

使用下列頂層區段：

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

核心教學欄位遵循 `soil-deck-core.md`。每張投影片再加入：

```yaml
visual: {mode: native, brief: "", source: ""}
interaction:
  type: stepper
  goal: "Understand the sequence"
  trigger: click
  initial_state: step_1
  states: [step_1, step_2, step_3]
  fallback: "Show all steps"
accessibility:
  keyboard: true
  touch: true
  reduced_motion: true
```

`interaction.type` 必須符合 `semantic_structure` 的允許路由。HTML 專屬的控制項、狀態、fallback 與中斷點不得混入共用核心欄位。
