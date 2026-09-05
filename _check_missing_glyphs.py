from fontTools.ttLib import TTFont
import os, sys
sys.stdout.reconfigure(encoding='utf-8')

fonts_dir = r"X:\14DaysWithYou-5.5-pc\game\tl\thai"
fpath = os.path.join(fonts_dir, "NotoSansThai-Body.ttf")
f = TTFont(fpath)
cmap = f.getBestCmap()

# Find missing Thai chars
missing = []
for c in range(0x0E00, 0x0E80):
    if c not in cmap:
        missing.append(c)

print(f"Missing {len(missing)} Thai chars in NotoSansThai-Body.ttf:")
for c in missing:
    print(f"  U+{c:04X} {chr(c)}")

f.close()
