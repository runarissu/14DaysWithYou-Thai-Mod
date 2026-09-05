from fontTools.ttLib import TTFont
import sys
sys.stdout.reconfigure(encoding='utf-8')

fpath = r"X:\14DaysWithYou-5.5-pc\_extracted\fonts\PlainPixel-Regular.ttf"
f = TTFont(fpath)
cmap = f.getBestCmap()

thai = sum(1 for c in range(0x0E00, 0x0E80) if c in cmap)
latin = sum(1 for c in range(0x0041, 0x007B) if c in cmap)
total = len(cmap)
print(f"PlainPixel: total={total} Thai={thai}/128 Latin={latin}/90")

# Check common Thai chars
common = "กขคงจฉชซญดตถทนบปผฝพฟภมยรลวศษสหฬอฮะาิีึืุู็่้๊๋์ัํฯๆๅ๐๑๒๓๔๕๖๗๘๙เแโใไ"
missing = [c for c in common if ord(c) not in cmap]
if missing:
    print(f"Missing common: {''.join(missing)} ({len(missing)} chars)")
else:
    print("All common Thai chars present!")

f.close()
