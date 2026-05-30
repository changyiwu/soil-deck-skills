# SOIL 簡報技能集（SOIL Deck Skills）

一組以 **李俊儀教授 SOIL Teaching Deck Workflow（六顆引擎）** 教學設計邏輯為核心的 **Agent Skills**，
專注於把教材／主題轉化為**有教學力的簡報**。三個技能對應三種輸出格式，可供 Claude Code 或任何支援 Agent Skills 規格的 AI agent 直接讀取使用。

> 所有技能皆以**繁體中文**設計。圖像由 OpenAI `gpt-image-2` 生成。

---

## 📦 包含的技能

| 技能 | 輸出格式 | 適用情境 | 額外檔案 |
|------|----------|----------|----------|
| [`soil-image-deck`](skills/soil-image-deck/SKILL.md) | `.pptx`（每頁一張 AI 全版圖） | 純圖片／全圖簡報，視覺震撼、像海報；每頁由 gpt-image-2 整頁生成 | `pack_pptx.py` |
| [`soil-teaching-deck`](skills/soil-teaching-deck/SKILL.md) | `.pptx`（文字可編輯 + AI 插圖） | 標準上課用投影片；混合「可編輯文字 + AI 插圖」，也能診斷／改善既有簡報 | — |
| [`soil-html-deck`](skills/soil-html-deck/SKILL.md) | 單一 `.html` | 自由度最高；可嵌互動圖表（Chart.js）、可點擊表格、影片、RWD、一鍵分享 URL，適合線上研習／直播 | — |

### 三者怎麼選

- 要**最快、最炫、整頁 AI 圖** → `soil-image-deck`
- 要**之後還能在 PowerPoint 改字** → `soil-teaching-deck`
- 要**互動、線上、可分享連結** → `soil-html-deck`

---

## 🚀 給其他 Agent 使用

純技能資料夾結構：

```bash
git clone https://github.com/mathruffian-dot/soil-deck-skills.git
```

讓你的 agent 讀取對應的 `skills/<技能名>/SKILL.md`，每份 frontmatter 都描述了觸發情境與操作步驟。

### 安裝到 Claude Code

```bash
# macOS / Linux
cp -r soil-deck-skills/skills/* ~/.claude/skills/

# Windows (PowerShell)
Copy-Item soil-deck-skills/skills/* $HOME/.claude/skills/ -Recurse
```

---

## ⚠️ 使用前注意（重要：外部依賴）

這三個技能都需要**生圖能力**，本 repo **未包含** `draw` 生圖技能本身。請先準備：

| 依賴 | 說明 |
|------|------|
| **`draw` 生圖技能** | 三個技能都呼叫 gpt-image-2 生圖腳本。SKILL.md 內有寫死的本機路徑 `C:/Users/mathr/.claude/skills/draw/draw.py`，外部使用時請**替換成你自己的 gpt-image-2 生圖工具路徑**。 |
| **`OPENAI_API_KEY`** | 生圖需要 OpenAI API key（設在 shell／`.env`／`~/.openai.env`）。gpt-image-2 需 OpenAI 組織完成 Individual 驗證。 |
| **Python + python-pptx** | `soil-image-deck/pack_pptx.py` 把生成的 PNG 打包成 `.pptx`，需 Python 環境。SKILL.md 內 `pack_pptx.py` 路徑也是寫死的本機路徑，請改成本 repo 內的相對路徑 `skills/soil-image-deck/pack_pptx.py`。 |

> 簡而言之：把 SKILL.md 內所有 `C:/Users/mathr/...` 路徑換成你環境的對應路徑，並備妥 OpenAI API key，即可使用。

---

## 📄 授權

MIT License，詳見 [LICENSE](LICENSE)。歡迎自由使用與修改。
