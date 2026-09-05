import re, os

dst_dir = r"X:\14DaysWithYou-5.5-pc\game\tl\thai\scripts\days"

for day in [3, 4, 5]:
    print(f"\n=== Day {day} ===")
    parts = []
    for fn in sorted(os.listdir(dst_dir)):
        if fn.startswith(f"day {day} - part ") and fn.endswith(".rpy"):
            full = os.path.join(dst_dir, fn)
            sz = os.path.getsize(full)
            if sz == 0:
                parts.append((fn, 0, 0))
                continue
            with open(full, "r", encoding="utf-8") as f:
                content = f.read()
            blocks = len(re.findall(r"^translate thai \w+:", content, re.MULTILINE))
            # find first and last label
            labels = re.findall(r"^translate thai (\w+):", content, re.MULTILINE)
            first = labels[0] if labels else ""
            last = labels[-1] if labels else ""
            parts.append((fn, blocks, sz, first, last))

    total_blocks = 0
    for p in parts:
        if len(p) == 5:
            print(f"  {p[0]}: {p[1]:>4} blocks  {p[2]:>7} bytes  first={p[3]}  last={p[4]}")
            total_blocks += p[1]
        else:
            print(f"  {p[0]}: EMPTY")
    print(f"  Total blocks in non-empty: {total_blocks}")
