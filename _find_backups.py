import os, glob

candidates = []
roots = [
    os.path.expandvars(r"%LOCALAPPDATA%"),
    os.path.expandvars(r"%APPDATA%"),
    r"C:\Users\lunas",
    r"X:\14DaysWithYou-5.5-pc",
]
# editor local history dirs
hist_patterns = [
    r"%LOCALAPPDATA%\Microsoft\VSCode\User\History",
    r"%LOCALAPPDATA%\Cursor\User\History",
    r"%LOCALAPPDATA%\Windsurf\User\History",
    r"%APPDATA%\Code\User\History",
    r"%APPDATA%\Cursor\User\History",
    r"%APPDATA%\Windsurf\User\History",
    r"%APPDATA%\devin",
]
print("=== Editor history dirs ===")
for p in hist_patterns:
    full = os.path.expandvars(p)
    if os.path.isdir(full):
        print("FOUND:", full)
        # walk one level
        try:
            for d in os.listdir(full)[:20]:
                print("  -", d)
        except Exception as e:
            print("  err", e)
    else:
        print("missing:", full)

# search for any file named like 'day 1*' anywhere in user profile and project
print("\n=== Search 'day 1*' .rpy files ===")
search_roots = [
    os.path.expandvars(r"%LOCALAPPDATA%"),
    os.path.expandvars(r"%APPDATA%"),
    r"X:\14DaysWithYou-5.5-pc",
    r"C:\Users\lunas\Documents",
    r"C:\Users\lunas\Desktop",
    r"C:\Users\lunas\Downloads",
]
for sr in search_roots:
    if not os.path.isdir(sr):
        continue
    for root, dirs, files in os.walk(sr):
        # skip huge dirs
        if "node_modules" in root or ".git" in root:
            continue
        for f in files:
            low = f.lower()
            if low.startswith("day 1") and low.endswith((".rpy", ".rpy.bak", ".rpy.tmp")):
                full = os.path.join(root, f)
                try:
                    sz = os.path.getsize(full)
                except Exception:
                    sz = -1
                if sz > 1000:
                    print(f"  {sz:>10}  {full}")
