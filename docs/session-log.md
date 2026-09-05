# Session Log

## 2026-09-05 — Thai Localization Mod Setup

### Decisions
- Engine: Ren'Py 8.5.2, scripts packed in `game/script.rpa`
- Used `unrpa` to extract scripts to `_extracted/`
- Used bundled `14DaysWithYou.exe` with `translate thai` CLI to generate translation framework
- Created temp project `_tmp_project/` with extracted scripts to generate dialog translation blocks (because main game only has .rpa)
- Font strategy: `config.font_replacement_map` with language callbacks (not `define gui.*_font`) to catch hardcoded font references in screens.rpy
- Pronoun strategy: wrap `refresh_pronouns()` in `replace_pronouns.rpy` — override to gender-neutral Thai when `_preferences.language == "thai"`
- Fonts: Sarabun (body), Prompt-SemiBold (names/headers), Prompt-Regular (UI) — copied from `C:\Windows\Fonts`

### Files Created
- `docs/thai-localization-mod-guide.md` — workflow guide
- `docs/en-th-localization-style-guide.md` — translation style guide
- `docs/codebase-map.md` — project structure reference
- `docs/active-task.md` — task tracker
- `game/tl/thai/replace_font.rpy` — font override via callbacks
- `game/tl/thai/replace_pronouns.rpy` — pronoun system override
- `game/tl/thai/common.rpy` — UI translations (needs fix: duplicate block)
- `game/tl/thai/scripts/**/*.rpy` — generated dialog translation blocks

### Issues Found
- `common.rpy`: SDK appended auto-generated `translate thai strings:` after my custom block → duplicate sections, need merge
- `replace_pronouns.rpy`: initial version called `refresh_pronouns()` at init time → `NameError: pronoun` not defined → fixed by removing the call
- Day 0 translation subagent was canceled before completion

### Next Steps
- Fix `common.rpy` duplicate blocks
- Restart day 0 translation with style guide context
- Parallelize day 1-5 translation with subagents

## 2026-09-05 — File Split for Safety

### Decision
- devin terminate หลายครั้ง เสียงานทั้งไฟล์ → แยกไฟล์ใหญ่เป็นไฟล์ย่อย
- แยก day 0-5 เป็น 88 ไฟล์ (รวม 6716 blocks)
- แยกตาม label prefix ถ้ามีหลาย prefix, ถ้า prefix เดียวแยกทุก 100 blocks
- ไฟล์ strings (choice/menu) แยกออกมาต่างหาก
- Original backup ที่ `_backup_days_original/`

### Status
- ทุกไฟล์ยังเป็นอังกฤษ (ยังไม่ได้แปล)
- พร้อมเริ่มแปลทีละไฟล์ย่อย

### Next Steps
- เริ่มแปล day 0 ทีละไฟล์ย่อย (10 ไฟล์)
- ไฟล์ไหนเสร็จ = เซฟ = เก็บถาวร

## 2026-09-05 — เปลี่ยน Font เป็น Noto Sans Thai

### Decision
- เปลี่ยน font ไทยจาก Sarabun/Prompt เป็น Noto Sans Thai (Google Fonts)
- ใช้ weight Regular + SemiBold + Bold
- Noto Sans Thai เป็น Thai-only (ไม่มี Latin) → ใช้ตรงๆ ใน font_replacement_map ไม่ได้
- แก้โดย merge Noto Sans Thai + font อังกฤษเดิม เป็น composite TTF ด้วย fontTools.merge

### Bug Fix
- script เดิมใช้ค่าเป็น string ใน font_replacement_map → ผิด (Ren'Py unpack เป็น 3 ค่า)
- แก้เป็น tuple `(filename, False, False)` ตามมาตรฐาน Ren'Py

### Files
- Composite fonts 8 ไฟล์ใน `game/tl/thai/NotoSansThai-*.ttf`
- `replace_font.rpy` อัปเดต mapping + แก้ bug

## 2026-09-05 — ติดตั้ง RTK + lean-ctx สำหรับ Devin Desktop

### Decisions
- พี่บอสใช้ Devin Desktop (ฝังเป็น Windsurf extension, CLI = `devin-desktop` v1.126.0)
- RTK v0.48.0 stable ยังไม่มี `--agent devin` (PR #3144 merge แล้วแต่อยู่ใน develop branch) → ใช้ `--agent windsurf` สำหรับ Cascade + เพิ่ม hook ให้ Devin CLI โดยตรงผ่าน `rtk hook claude` (format ตรงกับ Devin's PreToolUse + updatedInput)
- lean-ctx ลงผ่าน `npm install -g lean-ctx-bin` (v3.10.0)
- ตั้ง `shell_hook_disabled = true` ใน lean-ctx เพื่อไม่ให้ยุ่งกับ PowerShell profile — ปล่อยให้ rtk จัดการ shell compression ฝั่ง PowerShell แทน
- lean-ctx ทำงานเป็น MCP server (stdio) เท่านั้น ให้ `ctx_read`/`ctx_search`/`ctx_shell` ฯลฯ
- Node path เสถียร: `C:\Users\lunas\AppData\Roaming\fnm\node-versions\v26.8.1\installation\` (fnm default v26.8.1)

### Files Modified
- `C:\Users\lunas\.local\bin\rtk.exe` — RTK v0.48.0 binary (จาก GitHub release)
- `C:\Users\lunas\.windsurfrules` — RTK rules สำหรับ Windsurf Cascade
- `C:\Users\lunas\.config\lean-ctx\config.toml` — `shell_hook_disabled = true`
- `C:\Users\lunas\AppData\Roaming\devin\config.json` — เพิ่ม `hooks.PreToolUse` สำหรับ rtk
- `C:\Users\lunas\AppData\Roaming\devin\mcp_config.json` — เพิ่ม `lean-ctx` MCP server

### Next Steps
- Restart Devin Desktop เพื่อให้ hook + MCP server ใหม่มีผล
- ทดสอบ: สั่ง `git status` ใน Devin → ควรถูก rewrite เป็น `rtk git status` อัตโนมัติ
- ตรวจดู `ctx_*` tools ใน Devin (เช่น `ctx_read`, `ctx_search`)
