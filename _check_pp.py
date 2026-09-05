import zipfile, os, sys
sys.stdout.reconfigure(encoding='utf-8')

zip_path = r"X:\14DaysWithYou-5.5-pc\_tmp_pixelpoiiz.zip"
extract_dir = r"X:\14DaysWithYou-5.5-pc\_tmp_pixelpoiiz"

with zipfile.ZipFile(zip_path) as z:
    z.extractall(extract_dir)
    print("Files:", z.namelist())

from fontTools.ttLib import TTFont
for root, dirs, files in os.walk(extract_dir):
    for f in files:
        if f.endswith(".ttf"):
            fpath = os.path.join(root, f)
            font = TTFont(fpath)
            cmap = font.getBestCmap()
            thai = sum(1 for c in range(0x0E00, 0x0E80) if c in cmap)
            latin = sum(1 for c in range(0x0041, 0x007B) if c in cmap)
            total = len(cmap)
            print(f"\n{f}: total={total} Thai={thai}/128 Latin={latin}/90")
            font.close()
