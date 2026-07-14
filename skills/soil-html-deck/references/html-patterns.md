# SOIL HTML 模式

## 頁面框架

使用占滿視窗的投影片區段，包含進度列、SOIL 階段標籤、頁碼、明確導覽控制項，以及置中的安全區域容器。

```html
<main id="deck">
  <section class="slide active" data-slide="1" data-section="引起動機" data-interaction="none">...</section>
</main>
```

避免使用固定 1920×1080 畫布再以 transform 縮放。使用 CSS grid／flex、`clamp()`、長寬比與針對中斷點的重排。窄螢幕上應允許目前頁面垂直捲動，不要將文字縮小到無法閱讀。

## 設計系統

將 YAML token 對應到 CSS 自訂屬性：

```css
:root {
  --bg: #f5f1e8;
  --primary: #176b87;
  --accent: #f4a261;
  --ink: #173042;
  --title-size: clamp(2.1rem, 5vw, 4.6rem);
}
```

不得強制使用單一全域主題。保留使用者要求的色盤、材質、圓體字型、標題錨點、卡片語言與重複視覺母題。

## 受控元件

- `cover_hero`：主視覺素材加上即時行動呼籲／導覽。
- `question_focus`：一個問題與選用的漸進揭露。
- `comparison_split`：兩個即時面板，搭配切換或可排序證據。
- `process_timeline`：可點擊的步驟導覽，並顯示目前步驟說明。
- `classification_grid`：可篩選或選取的卡片。
- `relationship_map`：HTML 節點加上 SVG 連接線圖層。
- `case_scene_analysis`：輔助圖片加上分頁式解讀。
- `data_focus`：SVG／Canvas／圖表，搭配已宣告的控制項與文字摘要。
- `summary_three`：三個可選取的帶走重點。
- `action_next_step`：顯示結果的決策或行動呼籲。

## 導覽

支援 ArrowRight、Space、PageDown、ArrowLeft、PageUp、Home、End，以及用 `F` 進入全螢幕。提供可見的上一頁／下一頁按鈕。操作控制項、連結、表格標題、表單輸入或互動卡片時，不得觸發投影片導覽。

每次切換頁面都要更新進度、階段標籤、頁碼、焦點目標與 URL hash。明確綁定 DOM 參照；不得依賴瀏覽器從元素 ID 自動產生的全域變數。

## 無障礙與動態效果

- 使用語意化按鈕與焦點可見樣式。
- 為頁面與互動結果加入 `aria-live="polite"` 狀態區域。
- 每個指標裝置互動都必須提供鍵盤操作方式。
- 絕不能將必要內容藏在滑鼠懸停後方。
- 實作 `@media (prefers-reduced-motion: reduce)`。
- 圖片提供有意義的替代文字；純裝飾圖片則使用空白替代文字。

## 素材政策

使用 AI 生成或使用者提供的圖片作為主視覺或輔助素材。精確文案、公式、表格、圖解與互動標籤應保持即時可操作。最終圖片需嵌入為 data URI，以形成可攜式單一檔案。
