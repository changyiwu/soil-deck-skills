---
name: soil-image-deck
description: 建立 SOIL 風格、以圖片為核心的教學簡報，每張投影片皆由 AI 生成的全頁視覺主導。當使用者要求 SOIL 圖片簡報、純圖片教學投影片、NotebookLM 風格教育簡報、YAML 驅動的 SOIL 簡報、具視覺衝擊力的教師研習投影片，或遵循引起動機、維持注意、喚起行動與 SOIL 六引擎工作流的 baked/plate PPTX 時使用。
---

# SOIL 圖片簡報

運用 SOIL 教學判斷建立一致、以圖片為核心的簡報。先產出頁面計畫與 YAML 設計契約，再開始生成圖片；以黃金樣張鎖定風格，接著生成、檢查並封裝簡報。

規劃模型須與渲染器無關。同一份 SOIL 核心日後也能提供給 `soil-html-deck` 使用；圖片專屬的輸出欄位應歸在圖片渲染層。撰寫或遷移 YAML 前，先閱讀 `references/soil-deck-core.md`。

## 設定軸

- `output_mode`：`baked` 或 `plate`。
- `planning_mode`：`quick` 或 `yaml_spec`。
- `generation_strategy`：`sequential` 或 `subagents`。
- `style_lock`：`none` 或 `golden_sample`。

預設使用 `yaml_spec`、`sequential` 與 `golden_sample`。只有使用者明確要求平行生成，且環境允許時，才使用 `subagents`。

## 圖片硬性規則

- 每張投影片的視覺都必須優先使用 Codex 內建圖片生成功能製作。
- 不得用 Pillow、CSS、SVG、程序化圖形或預留位置取代圖片生成。
- 只有使用者明確要求時，才改用 API／CLI 圖片生成路徑。
- 封裝前，將每張採用的圖片儲存在專案內。

## 圓體字型政策

預設使用粗圓的繁體中文展示字：筆畫粗細均勻、端點柔和、字腔寬鬆、比例親切、轉角低銳度。

使用 `baked` 時，每則圖片提示詞都要重申圓體字型要求，並禁止尖角幾何中文字、窄長機械字、尖銳楔形與科技模板字。

使用 `plate` 時，依序採用系統已安裝的 `jf open 粉圓 2.1`、`GenSenRounded TW` 或 `GenJyuuGothic`。若都未安裝，預設改用 YAML `fallback_font_preferences` 中已安裝的可讀繁中字型，並在輸出記錄明確警告字型風格差異；將 `plate_font_fallback_policy` 設為 `strict` 時才停止封裝。

## SOIL 六引擎工作流

1. **概念定位**：定義一個總概念、三個子概念、常見誤解、帶走重點、最小事實包，以及投影片與口頭講述的分工。
2. **脈絡定位**：安排引起動機 → 維持注意 → 喚起行動。10 頁簡報的預設節奏約為 2／6／2。
3. **頁面架構**：每頁只設定一個角色、一個核心重點、一項學習任務、一種語意關係、一個 `layout.id`、最少可見文字與一份視覺簡述。
4. **認知編修**：檢查降雜訊、區塊化、增資訊、結構化、順脈絡、步驟化。
5. **風格建構**：依 `assets/soil-spec-template.yaml` 建立 `spec.yaml`；定義色盤、固定框架、圓體字型、版型路由、安全區域、圖片政策與驗證規則。
6. **製作**：驗證 YAML、核准黃金樣張、生成圖片、檢查蒙太奇總覽、針對失敗頁面重新生成、封裝 PPTX、再次渲染並驗證交付成果。

若使用者提供已驗證的 SOIL YAML 規格，只有在概念、流程、頁面角色與視覺系統都已明確定義時，才能略過引擎 1–5。

## 製作命令

驗證 YAML：

```powershell
python "<soil-image-deck-dir>\scripts\validate_spec.py" --spec .\spec.yaml
```

驗證生成圖片：

```powershell
python "<soil-image-deck-dir>\scripts\verify_images.py" --spec .\spec.yaml --images-dir .\slides\images
```

在 Codex 中，使用 Presentations skill 與 Artifact Tool 封裝。每張投影片嵌入一張滿版圖片，渲染匯出的 PPTX、檢查蒙太奇總覽，並執行溢位檢查。

若環境沒有 Artifact Tool，可使用 `scripts/pack_pptx.py` 作為可攜式備援方案。它會將 baked 圖片置中裁切成 16:9；在 `plate` 模式下優先使用圓體，必要時採用已宣告的可讀字型備援並顯示警告。

## 輸出模式

- `baked`：生成圖片內含精簡的可見文字。適合展示、社群分享、開場與視覺敘事。
- `plate`：生成無文字的設計底板並預留文字區，之後疊加可編輯文字。適合長期使用的教學簡報、後續修改、公式與精確資料。

當正確性很重要時，公式、精確幾何圖、圖表與數字證據應保留為原生可編輯元素。

## 參考文件

- 閱讀 `references/soil-engines.md`，了解必要的規劃輸出。
- 同一份計畫也可能產生互動 HTML 簡報時，閱讀 `references/soil-deck-core.md`。
- 撰寫 `spec.yaml` 前，閱讀 `references/yaml-profile.md`。
- 指派版型前，閱讀 `references/layout-recipes.md`。
- 生成圖片前，閱讀 `references/prompting.md`。
- 使用者要求平行生成時，閱讀 `references/subagent-batching.md`。
- 封裝與交付前，閱讀 `references/validation.md`。
