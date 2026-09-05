import re, os

# Analyze Day 3, 4, 5 to find content for the missing parts
# We need to figure out how the original split divided these days

days = [
    (r"X:\14DaysWithYou-5.5-pc\_backup_days_original\day 3.rpy", "day 3", r"X:\14DaysWithYou-5.5-pc\game\tl\thai\scripts\days"),
    (r"X:\14DaysWithYou-5.5-pc\_backup_days_original\day 4.rpy", "day 4", r"X:\14DaysWithYou-5.5-pc\game\tl\thai\scripts\days"),
    (r"X:\14DaysWithYou-5.5-pc\_backup_days_original\day 5.rpy", "day 5", r"X:\14DaysWithYou-5.5-pc\game\tl\thai\scripts\days"),
]

for src, dayname, dst_dir in days:
    print(f"\n=== {dayname} ===")
    with open(src, "r", encoding="utf-8") as f:
        lines = f.readlines()

    # Find all translate thai labels
    labels = []
    for i, line in enumerate(lines, 1):
        m = re.match(r"^translate thai (\w+):", line)
        if m:
            labels.append((i, m.group(1)))

    # Count existing split files
    existing = []
    for fn in os.listdir(dst_dir):
        if fn.startswith(f"{dayname} - part ") and fn.endswith(".rpy"):
            full = os.path.join(dst_dir, fn)
            sz = os.path.getsize(full)
            existing.append((fn, sz))

    existing.sort()
    total_blocks = len(labels)
    print(f"Total blocks: {total_blocks}")
    print(f"Existing split files: {len(existing)}")
    for fn, sz in existing:
        flag = "EMPTY" if sz == 0 else f"{sz} bytes"
        print(f"  {fn}: {flag}")

    # Count blocks per part (assuming equal split)
    non_empty = [(fn, sz) for fn, sz in existing if sz > 0]
    empty = [(fn, sz) for fn, sz in existing if sz == 0]
    print(f"Non-empty: {len(non_empty)}, Empty: {len(empty)}")
    print(f"Empty files: {[fn for fn, _ in empty]}")
