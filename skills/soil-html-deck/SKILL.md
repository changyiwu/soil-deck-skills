---
name: soil-html-deck
description: 建立由 YAML 驅動、可攜式單一檔案的 SOIL 互動 HTML 簡報。當使用者要求 HTML 簡報、互動投影片、網頁簡報、加入互動的 SOIL Image Deck、可點擊教學圖、響應式簡報頁面、可排序表格、圖表、決策樹、步驟導覽、測驗，或希望保留 SOIL 視覺規則並加入原生 HTML／CSS／JS 行為的簡報時使用。
---

# SOIL 互動 HTML 簡報

將 HTML 簡報視為 SOIL Image Deck 的互動上位輸出。共用相同的 SOIL 教學流程、頁面架構、設計系統、受控版型路由、圖片簡述與 YAML 核心。使用 HTML／CSS／JS 呈現即時文字與互動，而不是把簡報做成圖片輪播。

## 輸出契約

- 產出一個可直接用瀏覽器開啟、內嵌 CSS 與 JS 的 `.html` 檔案。
- 將採用的圖片嵌入為 `data:image/...;base64,...`，以便形成可攜式最終檔案。
- 標題、段落、標籤、卡片、表格、公式、圖表、決策節點與控制項須保留為即時 HTML、SVG、Canvas 或數學標記。
- 只有刻意設計的封面、章節分隔頁或結尾主視覺圖片可以使用 baked 文字。
- AI 視覺素材應使用內建圖片生成功能。不得用程序化預留圖取代使用者要求的 AI 視覺。
- 保留鍵盤、滑鼠與觸控導覽；加入減少動態效果的行為與無互動備援。

## 共用 SOIL 核心

從 `references/soil-deck-core.md` 中與渲染器無關的欄位開始，再依 `references/yaml-profile.md` 與 `assets/interactive-spec-template.yaml` 加入 HTML 互動與無障礙欄位。

使用下列設定軸：

- `planning_mode`：`quick` 或 `yaml_spec`；預設為 `yaml_spec`。
- `visual_mode`：`native`、`asset`、`plate`，或僅用於主視覺的 `baked`。
- `interaction_level`：`none`、`guided` 或 `exploratory`；預設為 `guided`。
- `portability`：`single_file` 或 `linked`；預設為 `single_file`。
- `style_lock`：`none` 或 `golden_trio`；預設為 `golden_trio`。

## 工作流

1. **概念與流程**：定義一個總概念、受眾成果、常見誤解，以及引起動機 → 維持注意 → 喚起行動。
2. **頁面架構**：每頁指派一項教學任務、一個核心重點、一項學習任務、一種語意結構、一個受控版型與精簡的可見文字。
3. **YAML 契約**：依 `assets/interactive-spec-template.yaml` 建立 `spec.yaml`；撰寫 HTML 前先鎖定設計、響應式行為、互動、無障礙與驗證規則。
4. **互動路由**：依意義而非裝飾選擇互動。閱讀 `references/interaction-router.md`。
5. **黃金三頁**：完整製作整份簡報前，先核准封面、標準內容頁與一張代表性互動頁。
6. **素材製作**：只生成必要圖片。即時 HTML 頁面優先使用無文字底板與輔助素材。
7. **HTML 製作**：使用 `references/html-patterns.md` 的元件與導覽模式；保留選定的主題，不強制套用固定的深色科技風。
8. **驗證**：驗證 YAML、嵌入素材、執行獨立檔案驗證器、在瀏覽器中檢查每一頁，並測試桌面與窄螢幕版面。

若已有通過驗證的 SOIL Image Deck YAML，應遷移其中與渲染器無關的欄位，不要重新開始規劃。加入 `learning_task`、`speaker_only`、`interaction`、`accessibility` 與響應式版型行為，再驗證升級後的規格。

## 互動政策

- 只有互動能釐清比較、順序、分類、因果、階層、資料、決策、練習或探索時才使用。
- 8–12 頁簡報預設安排 2–4 個有意義的互動；只有學習設計確實需要時才能增加。
- 每張投影片只保留一個主要互動。
- 每個互動都需要明確的學習目標、初始狀態、鍵盤／觸控操作與靜態備援。
- 不得將必要教學內容藏在只能用滑鼠懸停觸發的行為後方。
- 不得將動態效果當成裝飾；必須支援 `prefers-reduced-motion`。

## 字型與視覺規則

使用 YAML 設計系統。中文展示字預設維持粗體、圓潤、親切與低稜角。若本機已安裝，優先使用 `jf open 粉圓 2.1`、`GenSenRounded TW` 或 `GenJyuuGothic`；可攜式 HTML 則使用已宣告的圓體網頁字型或有文件說明的系統備援字型。

維持固定框架與受控變化：標題錨點、色盤、材質語言、重複視覺母題、安全區域與進度介面保持一致；版型與互動則依內容調整。

## 命令

驗證互動 YAML：

```powershell
python "<soil-html-deck-dir>\scripts\validate_interactive_spec.py" --spec .\spec.yaml
```

將生成的素材嵌入最終 HTML：

```powershell
python "<soil-html-deck-dir>\scripts\embed_assets.py" --template .\slides.template.html --output .\slides.html --asset COVER=.\assets\cover.png
```

驗證最終獨立簡報：

```powershell
python "<soil-html-deck-dir>\scripts\verify_html.py" --html .\slides.html --spec .\spec.yaml --strict-offline
```

## 參考文件

- 遷移或撰寫 YAML 前，閱讀 `references/soil-deck-core.md`。
- 建立互動規格時，閱讀 `references/yaml-profile.md`。
- 指派互動前，閱讀 `references/interaction-router.md`。
- 實作 HTML 前，閱讀 `references/html-patterns.md`。
- 交付前，閱讀 `references/validation.md`。
