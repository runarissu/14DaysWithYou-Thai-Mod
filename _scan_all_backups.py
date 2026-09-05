import os, glob

# Search the entire project and user profile for any .rpy file with Thai content
# that relates to day 1, day 3 part 02, day 4 part 09, day 5 part 05

targets = ["day 1", "day 3 - part 02", "day 4 - part 09", "day 5 - part 05"]

def has_thai(path, max_bytes=8000):
    try:
        with open(path, "rb") as f:
            raw = f.read(max_bytes)
        txt = raw.decode("utf-8", errors="replace")
        return any("\u0e00" <= c <= "\u0e7f" for c in txt)
    except Exception:
        return False

roots = [
    r"X:\14DaysWithYou-5.5-pc",
    r"C:\Users\lunas\AppData\Roaming\RenPy",
    r"C:\Users\lunas\AppData\Roaming\devin",
    r"C:\Users\lunas\Documents",
    r"C:\Users\lunas\Desktop",
    r"C:\Users\lunas\Downloads",
    r"C:\Users\lunas\OneDrive",
]

print("=== Scanning for target files with Thai content ===")
found = []
for root in roots:
    if not os.path.isdir(root):
        continue
    for r, dirs, files in os.walk(root):
        if ".git" in r or "node_modules" in r:
            continue
        # skip huge game lib
        if "lib" in r and "14DaysWithYou" in r:
            continue
        for fn in files:
            low = fn.lower()
            if not low.endswith((".rpy", ".rpy.bak", ".txt", ".md")):
                continue
            full = os.path.join(r, fn)
            try:
                sz = os.path.getsize(full)
            except Exception:
                continue
            if sz < 500:
                continue
            for t in targets:
                if t in fn.lower() or t in full.lower():
                    thai = has_thai(full)
                    found.append((full, sz, thai, t))
                    break

for full, sz, thai, t in sorted(found, key=lambda x: x[0]):
    flag = "THAI" if thai else "english/other"
    print(f"  [{flag:12}] {sz:>10}  target={t:20}  {full}")

print(f"\nTotal: {len(found)}")

# Also check Recycle Bin paths
print("\n=== Recycle Bin check ===")
for drive in ["C$", "X$"]:
    rb = f"\\\\?\\{drive[0]}:\\$Recycle.Bin"
    try:
        items = os.listdir(rb)
        print(f"  {rb}: {len(items)} entries")
    except Exception as e:
        print(f"  {rb}: {e}")
