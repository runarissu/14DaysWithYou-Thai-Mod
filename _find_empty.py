import os, sys
sys.stdout.reconfigure(encoding='utf-8')
d = r"X:\14DaysWithYou-5.5-pc\game\tl\thai\scripts\days"
for f in sorted(os.listdir(d)):
    if f.startswith("day 1") and f.endswith(".rpy"):
        p = os.path.join(d, f)
        sz = os.path.getsize(p)
        if sz < 200:
            print(f"{f}\t{sz} bytes")
