import zipfile, os, sys
sys.stdout.reconfigure(encoding='utf-8')

zip_path = r"X:\14DaysWithYou-5.5-pc\_tmp_plainpixel.zip"
extract_dir = r"X:\14DaysWithYou-5.5-pc\_tmp_plainpixel"

with zipfile.ZipFile(zip_path) as z:
    z.extractall(extract_dir)

for root, dirs, files in os.walk(extract_dir):
    for f in files:
        print(os.path.join(root, f))
