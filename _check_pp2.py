import zipfile, os, sys
sys.stdout.reconfigure(encoding='utf-8')

zip_path = r"X:\14DaysWithYou-5.5-pc\_tmp_pp2.zip"
extract_dir = r"X:\14DaysWithYou-5.5-pc\_tmp_pp2"

# Check if it's a zip
with open(zip_path, "rb") as f:
    magic = f.read(4)
    print(f"Magic bytes: {magic}")

if magic[:2] == b"PK":
    with zipfile.ZipFile(zip_path) as z:
        z.extractall(extract_dir)
        print("Files:", z.namelist())
else:
    # Maybe it's HTML
    with open(zip_path, "rb") as f:
        content = f.read(500)
        print("Content preview:", content[:200])
