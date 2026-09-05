import os, re, sys
sys.stdout.reconfigure(encoding='utf-8')

thai_dir = r"X:\14DaysWithYou-5.5-pc\game\tl\thai"

# Collect all "old" strings from ALL .rpy files, check for duplicates
all_olds = {}  # old_str -> [(file, line_num)]
for root, dirs, files in os.walk(thai_dir):
    for fname in files:
        if not fname.endswith(".rpy"):
            continue
        fpath = os.path.join(root, fname)
        relpath = os.path.relpath(fpath, thai_dir)
        with open(fpath, "r", encoding="utf-8") as f:
            for i, line in enumerate(f, 1):
                m = re.match(r'^\s+old "(.+)"\s*$', line)
                if m:
                    old_str = m.group(1)
                    if old_str in all_olds:
                        all_olds[old_str].append((relpath, i))
                    else:
                        all_olds[old_str] = [(relpath, i)]

dupes = {k: v for k, v in all_olds.items() if len(v) > 1}
print(f"Total old strings: {len(all_olds)}")
print(f"Duplicate old strings: {len(dupes)}")
for old, locations in dupes.items():
    print(f"  '{old[:50]}' -> {locations}")
