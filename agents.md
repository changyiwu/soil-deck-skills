# soil-deck-skills（專案藍圖）

> 本檔為跨 Agent 通用的專案藍圖（AGENTS.md 開放標準）。任何 Agent 的每個 session 都應先讀本檔＋`handoff.md`。

## 專案簡介

維護以 SOIL Teaching Deck Workflow 為核心的三套教學簡報 Skills：圖片簡報（`soil-image-deck`）、可編輯教學簡報（`soil-teaching-deck`）、互動 HTML 簡報（`soil-html-deck`）。三套皆具備可重現驗證與對應的 GitHub Actions CI。本專案未連結 Firebase，也未啟用部署。

## 關鍵時程

<!-- 目前無固定時程 -->

## 目標與路線圖

- [x] 階段一：三套 SOIL Skills 成形並可攜化
- [x] 階段二：統一 Image Deck v2 schema 與 `plate` 字型備援
- [x] 階段三：Teaching Deck 拆為可攜 Codex Skill；強化 HTML 單檔離線驗證
- [x] 階段四：新增一鍵驗證 `scripts/validate_all.py` 與三套 GitHub Actions workflow
- [ ] 階段五：後續維護直接在 `main` 進行，推送前先抓取並確認 `origin/main`
- [ ] 階段六：調整 Skills 理論或流程時，同步檢查 README、參考文件與交叉連結

## 資料夾結構

```
soil-deck-skills/
├─ skills/
│  ├─ soil-image-deck/SKILL.md      # 圖片簡報 Skill
│  ├─ soil-teaching-deck/SKILL.md   # 可編輯教學簡報 Skill
│  └─ soil-html-deck/SKILL.md       # 互動 HTML 簡報 Skill
├─ scripts/validate_all.py          # 一鍵驗證
├─ .github/workflows/               # 三套自動驗證 CI
├─ output/                          # 本機產出與相依套件（.gitignore 排除）
├─ requirements-dev.txt
├─ README.md                        # 使用與安裝說明
├─ agents.md                        # 本檔：專案藍圖
├─ handoff.md                       # 交接檔（每次收工必更新）
├─ .agents/  .gitignore
└─ LICENSE
```

## 同步層級（本專案初始化至第 3 層級）

| 層級 | 平台 | 位置 | 讀取時機 |
|------|------|------|---------|
| L1 | 本地（GDrive） | `agents.md`＋`handoff.md` | 每個 session |
| L2 | GitHub | origin：https://github.com/changyiwu/soil-deck-skills （公開）／upstream：`mathruffian-dot/soil-deck-skills` | 指定時 |
| L3 | Obsidian | `soil-deck-skills/專案工作流程.md` | 有需要時 |

> SOIL 理論來源（外部素材，唯讀）：`2ndbrain/01-Clippings/李俊儀-SOIL.md`。`01-Clippings/` 是外部輸入，除非使用者明確要求，不要改寫原始內容。

## 工作約定

- 任何 Agent、任何電腦：**開工先讀 `handoff.md`，收工必更新 `handoff.md`**
- 修改共用檔案前先讀最新內容，避免覆蓋其他 Agent 的變更
- 修改前先檢查 `git status`，保留不屬於目前任務的變更
- 使用繁體中文撰寫說明文件；程式碼、YAML 欄位、版型 ID、命令與必要的英文提示詞保持原樣
- 使用者要求 commit 或 push 時，預設直接提交並推送至 `changyiwu/soil-deck-skills` 的 `main`，不建立功能分支或 Pull Request；除非使用者當次另有指定
- 推送前先抓取並確認 `origin/main` 沒有未整合的新變更，**不使用 force push**
- `upstream` 只用來追蹤原始專案，**不作為預設推送目的地**，也勿動 `upstream/master`
- 更新 Obsidian 專案筆記時，不要修改 `02-知識庫/log.md`
- GDrive git 若遇 `FETCH_HEAD` 權限問題，設 `git config windows.appendAtomically=false`

## 驗證規則

- 修改任一 Skill 後執行 `python scripts/validate_all.py`（Windows 用 UTF-8 環境，`PYTHONUTF8=1`）
- 修改 Markdown 後，檢查本機連結、程式碼圍欄與 `git diff --check`
- 修改 `soil-image-deck` 後，驗證 `assets/soil-spec-template.yaml`
- 修改 `soil-html-deck` 後，驗證 `assets/interactive-spec-template.yaml`
- 產出的 PPTX、HTML、圖片、預覽、相依套件與暫存驗證結果一律放在 `output/`
- Image Deck `plate` 模式優先圓體，缺字時警告並用備援字型（嚴格風格設 `plate_font_fallback_policy: strict`）

## 安全邊界

- 不提交 `.env`、API Key、憑證、權杖、密碼、`.codex/`、`.claude/`、`.agents/`、`node_modules/` 或 `output/`
- 不在初始化流程中啟用部署、GitHub Pages、Firebase 或修改 Firebase 安全規則
- 不覆蓋既有 README、Skill 規則、Git 歷史或遠端設定；只做相容補充

## 最近進度

- 2026-07-24：專案藍圖改用標準範本格式（補上路線圖 checklist、資料夾結構與同步層級表）；L3 路徑由不存在的「專案駕駛艙.md」更正為 `soil-deck-skills/專案工作流程.md`，Clippings 路徑更正為 `01-Clippings/`。
