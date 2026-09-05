# Thai Localization Mod Guide — 14DaysWithYou 5.5 (Ren'Py 8.5.2)

> Senior modder workflow for adding Thai language support to a Ren'Py game whose scripts are packaged in `game/script.rpa`.

## Environment Summary

| Item | Value |
|---|---|
| Engine | **Ren'Py 8.5.2** |
| Script archive | `game/script.rpa` (~116 MB) |
| Existing `game/tl/` | None (no prior translation) |
| Bundled Python | 3.12 (`lib/py3-windows-x86_64`) |

---

## Step 1 — Extract `script.rpa`

`.rpa` is Ren'Py's archive format. You must extract it to `.rpy`/`.rpyc` before generating translations.

**Tool:** `unrpa`

```powershell
pip install unrpa
python -m unrpa -mp "X:\14DaysWithYou-5.5-pc\_extracted" "X:\14DaysWithYou-5.5-pc\game\script.rpa"
```

Output lands in `_extracted\game\`.

> ⚠️ Do NOT delete the original `script.rpa` — the game still needs it. Extraction is only for reference and mod building.

---

## Step 2 — Prepare Ren'Py SDK 8.5.2

Download the **exact matching** SDK from https://www.renpy.org/latest.html

- Extract SDK somewhere stable, e.g. `X:\renpy-8.5.2-sdk`
- Launch `renpy.exe`
- **Add Existing Project** → point at the game folder (or the extracted folder)

---

## Step 3 — Generate Translation Framework

In the Ren'Py Launcher:

1. Open the project
2. Click **"Generate Translations"**
3. Enter language code: `thai` (or `th`)
4. Launcher creates `game/tl/thai/` containing:
   - `common.rpy` — default Ren'Py UI strings (Save/Load/Preferences/Menu)
   - `script.rpy` — all dialog lines (`old "..."` / `new "..."`)

CLI equivalent:

```powershell
& "X:\renpy-8.5.2-sdk\renpy.exe" "X:\14DaysWithYou-5.5-pc" translate thai
```

---

## Step 4 — Configure Thai Fonts (Critical)

Thai script requires a font with full Thai glyph coverage and correct combining marks. Override the game's default fonts.

Create `game/tl/thai/replace_font.rpy`:

```renpy
# Replace the game's default fonts with Thai-capable ones
define gui.text_font = "tl/thai/Sarabun-Regular.ttf"
define gui.text_bold_font = "tl/thai/Sarabun-Bold.ttf"
define gui.name_text_font = "tl/thai/Sarabun-Bold.ttf"
define gui.interface_text_font = "tl/thai/Sarabun-Regular.ttf"
define gui.button_text_font = "tl/thai/Sarabun-Regular.ttf"

# Disable any English-only font replacement map
define config.font_replacement_map = { }
```

Place Thai-capable `.ttf` files in `game/tl/thai/`.

**Recommended fonts (OFL/Apache, free):**

- **Noto Sans Thai** — Google, full coverage, safe default
- **Sarabun** — designed for Thai on-screen reading
- **Kanit** / **Prompt** — modern, geometric
- **IBM Plex Sans Thai** — corporate clean

---

## Step 5 — Enable Correct Thai Line Breaking

Ren'Py's default line breaker does not segment Thai (no spaces between words). Install `PyICU` for proper ICU line breaking.

```powershell
pip install PyICU --target "X:\14DaysWithYou-5.5-pc\game\python-packages"
```

Add to `game/tl/thai/replace_font.rpy`:

```renpy
init python:
    try:
        import icu
        config.line_buffering_function = None
    except ImportError:
        pass

    # Thai glyphs often need a touch more vertical breathing room
    style.text.line_leading = 2
    style.text.line_spacing = 0
```

If word breaking is still poor without ICU, consider pre-segmenting translated strings with a Thai word breaker (e.g. `pythainlp`) and inserting zero-width spaces (`\u200b`) at break points.

---

## Step 6 — Translate All Strings

Open `game/tl/thai/script.rpy`. Format:

```renpy
translate thai start_1:
    # "Hello, how are you?"
    new "สวัสดี เป็นยังไงบ้าง?"
```

Translate every `old` → `new`. Repeat for `common.rpy` (UI).

**Senior tips:**

- Extract all strings to CSV, translate in a spreadsheet or PO editor, then merge back with a Python script.
- Preserve Ren'Py variable interpolation exactly: `{w}`, `{b}`, `[name]`, `[player_name]`
- Preserve text tags: `{size=20}`, `{color=#fff}`, `{i}...{/i}` — never translate or break them
- Dynamic character names (`[name]`) must stay as variables, not hardcoded Thai
- Watch for pluralization blocks and string comparisons in code that may break if a translated string is compared by identity

---

## Step 7 — Add a Language Selector

Add a switch button to the Preferences screen (in `replace_font.rpy` or a new file):

```renpy
screen preferences():
    # ... existing content ...
    hbox:
        textbutton _("English") action Language(None)
        textbutton _("ไทย") action Language("thai")
```

Quick test from console:

```renpy
$ renpy.change_language("thai")
```

---

## Step 8 — Package the Mod as an Archive (Recommended)

Keeps the mod clean and separate from the base game files.

Using Ren'Py SDK:

```powershell
& "X:\renpy-8.5.2-sdk\renpy.exe" "X:\14DaysWithYou-5.5-pc" package
```

Or using `rpatool` / `rpa`:

```powershell
pip install rpa
python -m rpa create thai_mod.rpa game/tl/thai/
```

Drop the resulting `thai_mod.rpa` into `game/`. Ren'Py auto-loads it as an overlay.

---

## Final Mod Layout

```
14DaysWithYou-5.5-pc\
└── game\
    ├── thai_mod.rpa          # optional packaged form
    └── tl\
        └── thai\
            ├── common.rpy    # UI strings
            ├── script.rpy    # dialog
            ├── replace_font.rpy
            ├── Sarabun-Regular.ttf
            ├── Sarabun-Bold.ttf
            └── NotoSansThai-Regular.ttf
```

---

## Common Pitfalls

| Problem | Fix |
|---|---|
| Original font has no Thai glyphs → `□□□` boxes | Override every font the game uses (check the game's `gui.rpy`) |
| Thai words don't wrap, overflow the textbox | Install `PyICU`, or pre-segment with `pythainlp` + ZWSP |
| Thai text looks smaller than English at same pt size | Bump `gui.text_size` by 1–2 pt |
| Thai combining marks / vowels don't render | Use a font with full Thai shaping (Noto Sans Thai, Sarabun) |
| Game update overwrites `script.rpa` and kills the mod | Keep mod as a separate `.rpa`, never edit the base archive |
| Font licensing | Use only OFL/Apache fonts (Noto, Sarabun, Kanit, Prompt) |

---

## Tooling Summary

| Tool | Purpose |
|---|---|
| `unrpa` | Extract `.rpa` archives |
| Ren'Py SDK 8.5.2 | Generate translations, package mod |
| `rpatool` / `rpa` | Repackage mod into `.rpa` |
| `PyICU` | Correct Thai line breaking |
| `pythainlp` (optional) | Thai word segmentation fallback |
| Noto Sans Thai / Sarabun | Thai-capable fonts (OFL) |
