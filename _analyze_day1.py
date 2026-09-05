import re

src = r"X:\14DaysWithYou-5.5-pc\_backup_days_original\day 1.rpy"
with open(src, "r", encoding="utf-8") as f:
    lines = f.readlines()

# Find all translate thai labels and their line numbers
labels = []
for i, line in enumerate(lines, 1):
    m = re.match(r"^translate thai (\w+):", line)
    if m:
        labels.append((i, m.group(1)))

# Group by label prefix (strip hash suffix)
groups = {}
for ln, lab in labels:
    prefix = re.sub(r"_[a-f0-9]+$", "", lab)
    groups.setdefault(prefix, []).append((ln, lab))

print(f"Total blocks: {len(labels)}")
print(f"Total groups: {len(groups)}")
print()
for p, items in groups.items():
    print(f"  {p}: {len(items)} blocks (lines {items[0][0]}-{items[-1][0]})")
