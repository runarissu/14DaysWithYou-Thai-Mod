import os, re, sys
sys.stdout.reconfigure(encoding='utf-8')

base = r"X:\14DaysWithYou-5.5-pc\game\tl\thai\scripts"
groups = {"days": [], "misc": [], "common": []}
for sub in groups:
    d = os.path.join(base, sub)
    if not os.path.isdir(d):
        continue
    for fn in sorted(os.listdir(d)):
        if fn.endswith(".rpy"):
            p = os.path.join(d, fn)
            with open(p, "r", encoding="utf-8") as f:
                content = f.read()
            blocks = len(re.findall(r'^translate thai \S+:', content, re.MULTILINE))
            groups[sub].append((fn, os.path.getsize(p), blocks))

for sub in ["days", "misc", "common"]:
    print(f"\n=== {sub} ({len(groups[sub])} files) ===")
    total = 0
    for fn, sz, bl in groups[sub]:
        if fn.startswith("day 0"):
            continue
        total += bl
        print(f"  {fn:45s} {bl:4d} blocks  {sz:7d} bytes")
    print(f"  TOTAL (excl day 0): {total} blocks")
