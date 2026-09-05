from fontTools.ttLib import TTFont
import os

fonts_dir = r"X:\14DaysWithYou-5.5-pc\game\tl\thai"
fonts = [
    "NotoSansThai-Body.ttf",
    "NotoSansThai-Bold.ttf",
    "NotoSansThai-Flow.ttf",
    "NotoSansThai-Names.ttf",
    "NotoSansThai-Reenie.ttf",
    "NotoSansThai-Regular.ttf",
    "NotoSansThai-SemiBold.ttf",
    "NotoSansThai-UI.ttf",
    "NotoSansThai-UIAlt.ttf",
    "NotoSansThai-Underdog.ttf",
    "NotoSansThai-VT323.ttf",
    "Prompt-Regular.ttf",
    "Prompt-SemiBold.ttf",
    "Sarabun-Regular.ttf",
]

for fname in fonts:
    fpath = os.path.join(fonts_dir, fname)
    if not os.path.exists(fpath):
        print(f"  MISSING: {fname}")
        continue
    f = TTFont(fpath)
    cmap = f.getBestCmap()
    # Check Thai range U+0E00 to U+0E7F
    thai_chars = sum(1 for c in range(0x0E00, 0x0E80) if c in cmap)
    # Check Latin
    latin_chars = sum(1 for c in range(0x0041, 0x007B) if c in cmap)
    print(f"  {fname}: Thai={thai_chars}/128 Latin={latin_chars}/90")
    f.close()
