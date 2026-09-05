from fontTools.ttLib import TTFont
import os, sys
sys.stdout.reconfigure(encoding='utf-8')

fonts_dir = r"X:\14DaysWithYou-5.5-pc\game\tl\thai"

# Common Thai characters used in everyday text
common_thai = "กขฃคฅฆงจฉชซฌญฎฏฐฑฒณดตถทธนบปผฝพฟภมยรลวศษสหฬอฮะาิีึืุู็่้๊๋์๎์ัํฺฯๆๅ๐๑๒๓๔๕๖๗๘๙"
# Add combining marks and vowels
common_thai += "เแโใไ็่้๊๋์ะาิีึืุูัํฺฯๆๅ๐๑๒๓๔๕๖๗๘๙"
# Remove duplicates
common_thai = "".join(dict.fromkeys(common_thai))

fonts = [
    "NotoSansThai-Body.ttf",
    "NotoSansThai-Names.ttf",
    "NotoSansThai-UI.ttf",
    "NotoSansThai-UIAlt.ttf",
    "NotoSansThai-Underdog.ttf",
    "NotoSansThai-VT323.ttf",
    "NotoSansThai-Flow.ttf",
    "NotoSansThai-Reenie.ttf",
]

for fname in fonts:
    fpath = os.path.join(fonts_dir, fname)
    f = TTFont(fpath)
    cmap = f.getBestCmap()
    missing = [c for c in common_thai if ord(c) not in cmap]
    if missing:
        print(f"  {fname}: MISSING {len(missing)} common chars: {''.join(missing)}")
    else:
        print(f"  {fname}: OK (all common chars present)")
    f.close()
