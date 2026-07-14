# SOIL 圖片提示詞契約

依下列順序組合提示詞：

1. 完整的 16:9 投影片圖片與安全區域。
2. 受控版型與閱讀動線。
3. 教學視覺與資訊關係。
4. `baked` 模式中要出現的精確文字。
5. 共用風格與黃金樣張參考。
6. 圓體繁體中文字型。
7. 負面提示詞。

圓體字型區塊：

```text
Typography: bold rounded Traditional Chinese display lettering with thick even
strokes, soft terminals, generous counters, friendly proportions, and low corner
sharpness. Avoid angular geometric Chinese type, condensed mechanical forms,
sharp wedges, thin strokes, or techno-stencil lettering. Render only the quoted
text, exactly once, with no extra characters.
```

必須說明輸出內容就是投影片本身，而不是螢幕、投影幕或模型展示圖。

使用 `plate` 模式時，禁止出現任何文字，並依最終疊字版型在周圍生成平靜、留白充足的保留區。
