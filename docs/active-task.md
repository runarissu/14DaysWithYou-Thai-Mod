# Active Task — Thai Localization Mod

## Task
Build a complete Thai localization mod for 14 Days With You 5.5 (Ren'Py 8.5.2).

## Scope
- Translate ~6,716 dialog blocks across day 0-5 + misc files
- Translate UI strings (common.rpy)
- Override fonts for Thai rendering
- Override dynamic pronoun system for gender-neutral Thai
- Add language selector
- Package as distributable mod

## File Structure (Split for Safety)
Each day's `.rpy` was split into multiple smaller files so that if devin terminates mid-translation, completed files are preserved.

- Split by label prefix when available (e.g. `deadend1`, `foxren`, `meet`, `sleeping`)
- Single-prefix days split by 100 blocks/file (`part 01`, `part 02`, ...)
- `strings.rpy` separated for choice/menu strings
- Original files backed up to `_backup_days_original/`

| Day | Files | Total Blocks |
|---|---|---|
| day 0 | 10 | 379 |
| day 1 | 18 | 918 |
| day 2 | 12 | 1040 |
| day 3 | 15 | 1346 |
| day 4 | 18 | 1691 |
| day 5 | 15 | 1342 |
| **Total** | **88** | **6716** |

## Current Status

| Step | Status | Notes |
|---|---|---|
| Extract script.rpa | ✅ Done | `_extracted/` |
| Write style guide | ✅ Done | `docs/en-th-localization-style-guide.md` |
| Generate translation framework | ✅ Done | SDK generated all blocks |
| Set up Thai fonts | ✅ Done | Sarabun + Prompt copied |
| Override pronoun system | ✅ Done | `replace_pronouns.rpy` |
| Translate UI (common.rpy) | ✅ Done | Merged & translated |
| Split day files | ✅ Done | 88 files in `game/tl/thai/scripts/days/` |
| Translate day 0 | ⏳ Pending | 10 files |
| Translate day 1 | ⏳ Pending | 18 files |
| Translate day 2 | ⏳ Pending | 12 files |
| Translate day 3 | ⏳ Pending | 15 files |
| Translate day 4 | ⏳ Pending | 18 files |
| Translate day 5 | ⏳ Pending | 15 files |
| Translate other files | ⏳ Pending | misc/*.rpy |
| Add language selector | ⏳ Pending | |
| Test in-game | ⏳ Pending | |
| Package mod | ⏳ Pending | |

## Translation Strategy
- หนูแปลเองทีละไฟล์ย่อย (ประมาณ 50-100 blocks ต่อไฟล์)
- แปลเสร็จไฟล์ไหน เซฟไฟล์นั้น → เก็บไว้ถาวร
- ถ้า devin terminate กลางทาง → เสียแค่ไฟล์ที่กำลังทำอยู่
- ลำดับความสำคัญ: เนื้อเรื่องหลัก > yandere scene > easter egg > glitch text

## Known Issues
1. Subagent ไม่น่าเชื่อถือ — หนูแปลเองทั้งหมด
2. ต้องลบ .rpyc เดิมก่อนรันเกม เพื่อให้ Ren'Py recompile จาก .rpy ใหม่

## Key References
- Style guide: `docs/en-th-localization-style-guide.md`
- Mod guide: `docs/thai-localization-mod-guide.md`
- Codebase map: `docs/codebase-map.md`
- Backup: `_backup_days_original/`
