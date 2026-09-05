# Codebase Map — 14DaysWithYou 5.5

## Project Overview

| Item | Value |
|---|---|
| Game | 14 Days With You (visual novel) |
| Engine | Ren'Py 8.5.2 |
| Version | 5.5 |
| Developer | cutiesai (Saint) |
| Platform | Windows (PC) |
| Path | `X:\14DaysWithYou-5.5-pc` |

## Directory Structure

```
14DaysWithYou-5.5-pc/
├── 14DaysWithYou.exe          # Game launcher
├── 14DaysWithYou.py           # Ren'Py bootstrap
├── 14DaysWithYou.sh           # Linux/Mac launcher
├── game/                      # Game data
│   ├── script.rpa             # Packed scripts (~116 MB)
│   ├── cache/
│   ├── python-packages/       # discord_rpc, requests, etc.
│   └── tl/thai/               # Thai localization mod (NEW)
│       ├── common.rpy         # UI strings translation
│       ├── replace_font.rpy   # Font override
│       ├── replace_pronouns.rpy # Pronoun system override
│       ├── Sarabun-Regular.ttf
│       ├── Prompt-Regular.ttf
│       ├── Prompt-SemiBold.ttf
│       └── scripts/           # Dialog translation blocks
│           ├── common/        # options, screens
│           ├── days/          # day 0-5
│           └── misc/          # other, gallery, unlockables
├── renpy/                     # Ren'Py engine runtime
├── lib/                       # Python 3.12 runtime
└── docs/                      # Documentation (NEW)
    ├── thai-localization-mod-guide.md
    └── en-th-localization-style-guide.md
```

## Key Files

### Scripts (extracted to `_extracted/scripts/`)

| File | Purpose | Lines |
|---|---|---|
| `common/script.rpy` | Empty (organizational) | 6 |
| `common/options.rpy` | Game config, build settings | 217 |
| `common/gui.rpy` | GUI variables, fonts, colors | 489 |
| `common/screens.rpy` | All UI screens (menu, save, prefs) | 1889 |
| `days/day 0.rpy` | Dead ends (bad endings) | 836 |
| `days/day 1.rpy` | Day 1 — meet Violet, work | 2009 |
| `days/day 2.rpy` | Day 2 | 2268 |
| `days/day 3.rpy` | Day 3 | 2630 |
| `days/day 4.rpy` | Day 4 (largest) | 3442 |
| `days/day 5.rpy` | Day 5 | 3065 |
| `misc/characters.rpy` | Character definitions | 56 |
| `misc/variables.rpy` | Game state variables | 443 |
| `misc/other.rpy` | Customization, socials, misc screens | 4475 |
| `misc/gallery.rpy` | Gallery screen | 419 |
| `misc/unlockables.rpy` | Unlock system | 119 |

### Characters (from `misc/characters.rpy`)

| Variable | Name | Color | Type |
|---|---|---|---|
| `r` | Ren | #ff66cb | Main (yandere) |
| `m` / `mt` / `mcall` | Moth | #5269b9 | Friend |
| `v` / `vt` / `vcall` | Violet | #c6b3f8 | Neighbor |
| `e` / `et` / `ecall` | Elanor | #d8c365 | Motherly |
| `c` / `ct` / `ccall` | Conan | #98d2ff | Librarian |
| `j` / `jt` / `jcall` | Jae | #faa97e | Partygoer |
| `l` / `lt` / `lcall` | Leon | #ee6c6d | Shy |
| `t` / `tt` / `tcall` | Teo | #93b482 | Prankster |
| `o` / `ot` / `ocall` | Olivia | #a8a7a7 | Bold |
| `k` / `kt` / `kcall` | Kiara | #b18f84 | Merchant |
| `n` | Narrator | None | Player thoughts |
| `y` | Player | [player] | Player speech |
| `npc` | ??? | #f8f8f8 | Unknown |
| `rfade` | (centered) | None | Void Ren |

### Dynamic Pronoun System (from `misc/variables.rpy`)

Variables set by `refresh_pronouns()` in `misc/other.rpy`:
- `they`, `them`, `their`, `theirs`, `themself`
- `person`, `baby`, `partner`, `spouse`, `are`, `gorgeous`
- 48 dialog insertion points across all day files

### Fonts (from `common/gui.rpy`)

| Variable | Font | Purpose |
|---|---|---|
| `gui.text_font` | VarelaRound-Regular.ttf | Body text |
| `gui.name_text_font` | Orbitron-Black.ttf | Character names |
| `gui.interface_text_font` | Assistant-Regular.ttf | UI text |

## Translation Stats

| File | Blocks |
|---|---|
| day 0 | 379 |
| day 1 | 918 |
| day 2 | 1040 |
| day 3 | 1346 |
| day 4 | 1691 |
| day 5 | 1342 |
| other | 12 |
| unlockables | 70 |
| **Total** | **~5,800** |
