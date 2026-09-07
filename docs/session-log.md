# Session Log

## 2026-09-05 — Thai Localization Mod Setup

### Decisions
- Engine: Ren'Py 8.5.2, scripts packed in `game/script.rpa`
- Used `unrpa` to extract scripts to `_extracted/`
- Used bundled `14DaysWithYou.exe` with `translate thai` CLI to generate translation framework
- Created temp project `_tmp_project/` with extracted scripts to generate dialog translation blocks
- Font strategy: `config.font_replacement_map` with language callbacks
- Pronoun strategy: wrap `refresh_pronouns()` in `replace_pronouns.rpy` for gender-neutral Thai
- Fonts: later changed to composite Noto Sans Thai + original English font

### Files Created
- `docs/thai-localization-mod-guide.md`
- `docs/en-th-localization-style-guide.md`
- `docs/codebase-map.md`
- `docs/active-task.md`
- `game/tl/thai/replace_font.rpy`
- `game/tl/thai/replace_pronouns.rpy`
- `game/tl/thai/common.rpy`
- `game/tl/thai/scripts/**/*.rpy`

### Issues / Fixes
- `common.rpy`: SDK duplicate string block identified; needs merge review
- `replace_pronouns.rpy`: removed premature `refresh_pronouns()` call causing `NameError`
- Day 0 translation was previously canceled before completion

## 2026-09-05 — File Split for Safety

### Decision
- Split day 0-5 into 88 files (6716 blocks) so completed files survive interruptions.
- Split by label prefix where possible; otherwise roughly 100 blocks/file.
- Separate `strings` files for choices/menus.
- Original backups stored in `_backup_days_original/`.

## 2026-09-05 — Font Update

### Decision
- Changed Thai font strategy to composite Noto Sans Thai + original English font.
- Fixed `font_replacement_map` values to Ren'Py tuple format `(filename, False, False)`.

## 2026-09-07 — Full Thai Localization QA

### Workflow
- QA one Day end-to-end before moving to the next: source/Thai meaning, natural Thai, spelling, grammar, character voice, punctuation, and Ren'Py tags/variables.
- Do not stop mid-Day or claim completion from sampling.

### Day 0
- Completed review of all 10 Day 0 translation files: deadend1-5, eastereggalternative, monsterpupeasteregg, part 01, part 02, strings.
- Corrected confirmed issues including `ปริว`→`ปลิว`, malformed phrases, unnatural literal translations, `ดีตา` usage in dialogue, punctuation, and several awkward English-to-Thai constructions.
- Preserved intentional glitch/cipher text and Ren'Py formatting tags.
- Status: complete.

### Day 1
- Completed review of all 16 active Day 1 Thai `.rpy` translation files: meet, mothaltintro, mothaltending, nowahoo, part 01-05, reninterrupt, saygoodnight, saynothing, sleeping, sleepingbed, sleepingfloor, strings.
- Corrected confirmed typos, unnatural literal phrasing, malformed Thai, repeated/incorrect words, and several context-sensitive dialogue/narration issues.
- Preserved intentional glitch/cipher text and Ren'Py formatting tags/variables.
- Status: complete.

### Day 2
- Completed review of all 12 active Day 2 Thai `.rpy` translation files: part 01-11 and strings.
- Corrected confirmed typos, malformed Thai, unnatural literal phrasing, timing/wording errors, and context-sensitive dialogue/narration issues.
- Preserved intentional glitch/cipher text and Ren'Py formatting tags/variables.
- Status: complete.

### Day 3
- Completed review of all 15 active Day 3 Thai `.rpy` translation files: part 01-14 and strings.
- Corrected confirmed typos, malformed Thai, unnatural/literal phrasing, and context-sensitive dialogue/narration issues across the day.
- Preserved intentional glitch/cipher text and Ren'Py formatting tags/variables/placeholders.
- `git diff --check` passes for Day 3 files.
- Status: complete.

### Day 4
- Completed review of all 18 active Day 4 Thai `.rpy` translation files: part 01-17 and strings.
- Corrected confirmed typos, malformed Thai, unnatural/literal phrasing, duplicate wording, placeholder spacing issues, and context-sensitive dialogue/narration issues.
- Preserved intentional glitch/cipher text and Ren'Py formatting tags/variables/placeholders.
- `git diff --check` passes for Day 4 files.
- Status: complete.

### Day 5
- Completed review of all 15 active Day 5 Thai `.rpy` translation files: part 01-14 and strings.
- Corrected confirmed typos, malformed Thai, unnatural/literal phrasing, terminology issues, punctuation/spacing issues, and context-sensitive dialogue/narration problems.
- Preserved intentional glitch/cipher text and Ren'Py formatting tags/variables/placeholders.
- `git diff --check` passes for Day 5 files.
- Status: complete.

### Next
- Day 5 QA is complete. Continue to the next requested localization task/day.