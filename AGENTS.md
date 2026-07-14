# soil-deck-skills 專案規則

## 專案概要

- **用途**：維護以 SOIL Teaching Deck Workflow 為核心的三套教學簡報 Skills。
- **本機路徑**：`C:\Users\chang\我的雲端硬碟\agents\soil-deck-skills`
- **GitHub origin**：`https://github.com/changyiwu/soil-deck-skills.git`
- **GitHub upstream**：`https://github.com/mathruffian-dot/soil-deck-skills.git`
- **預設分支**：`master`
- **Firebase**：未連結。
- **部署**：未啟用 GitHub Pages 或其他部署。

## 專案入口

- 使用與安裝說明：`README.md`
- 圖片簡報 Skill：`skills/soil-image-deck/SKILL.md`
- 可編輯教學簡報 Skill：`skills/soil-teaching-deck/SKILL.md`
- 互動 HTML 簡報 Skill：`skills/soil-html-deck/SKILL.md`
- 自動驗證：`.github/workflows/`
- 本機產出：`output/`，只供驗證與預覽，不納入 Git。

## 第二大腦連結

- 主要 Vault：`C:\Users\chang\我的雲端硬碟\2ndbrain`
- 專案駕駛艙：`C:\Users\chang\我的雲端硬碟\2ndbrain\soil-deck-skills-專案駕駛艙.md`
- SOIL 理論來源：`C:\Users\chang\我的雲端硬碟\2ndbrain\Clippings\李俊儀-SOIL.md`
- 開工時先讀專案駕駛艙；收工時更新駕駛艙的最後動作、狀態、下一步、變更紀錄與踩坑筆記。
- 建立、移動、改名或更新專案駕駛艙時，不要修改 `知識庫/log.md`。
- `Clippings/` 是外部輸入，除非使用者明確要求，不要改寫原始內容。

## 工作與同步規則

- 修改前先檢查 `git status`，保留不屬於目前任務的變更。
- 使用繁體中文撰寫說明文件；程式碼、YAML 欄位、版型 ID、命令與必要的英文提示詞保持原樣。
- 當使用者要求 commit 或 push 時，預設直接提交並推送至 `changyiwu/soil-deck-skills` 的 `master`，不建立功能分支或 Pull Request；除非使用者當次另有指定。
- 推送前先抓取並確認 `origin/master` 沒有未整合的新變更，不使用 force push。
- `upstream` 只用來追蹤原始專案，不作為預設推送目的地。

## 驗證規則

- 修改 Markdown 後，檢查本機連結、程式碼圍欄與 `git diff --check`。
- 修改 `soil-image-deck` 後，驗證 `assets/soil-spec-template.yaml`。
- 修改 `soil-html-deck` 後，驗證 `assets/interactive-spec-template.yaml`。
- 產出的 PPTX、HTML、圖片、預覽、相依套件與暫存驗證結果一律放在 `output/`。

## 安全邊界

- 不提交 `.env`、API Key、憑證、權杖、密碼、`.codex/`、`.claude/`、`.agents/`、`node_modules/` 或 `output/`。
- 不在初始化流程中啟用部署、GitHub Pages、Firebase 或修改 Firebase 安全規則。
- 不覆蓋既有 README、Skill 規則、Git 歷史或遠端設定；只做相容補充。
