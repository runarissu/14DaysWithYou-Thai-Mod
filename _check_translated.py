import os, re, sys
sys.stdout.reconfigure(encoding='utf-8')

dst_dir = r"X:\14DaysWithYou-5.5-pc\game\tl\thai\scripts\days"

# Check all Day 1 files + Day 3/4/5 parts
files_to_check = []
for fn in sorted(os.listdir(dst_dir)):
    if fn.startswith("day 1") and fn.endswith(".rpy"):
        files_to_check.append(fn)
    elif fn in ("day 3 - part 02.rpy", "day 4 - part 09.rpy", "day 5 - part 05.rpy"):
        files_to_check.append(fn)

print(f"{'File':<40} {'Size':>8} {'Blocks':>7} {'Has Thai':>10} {'Status':>15}")
print("-" * 85)
for fn in files_to_check:
    full = os.path.join(dst_dir, fn)
    sz = os.path.getsize(full)
    with open(full, "r", encoding="utf-8") as f:
        content = f.read()
    blocks = len(re.findall(r"^translate thai \w+:", content, re.MULTILINE))
    # Check if has Thai characters in dialog lines (not just comments)
    has_thai = bool(re.search(r'^    [a-z]+ ".*[\u0e00-\u0e7f]', content, re.MULTILINE))
    # Count untranslated lines (dialog lines still in English)
    dialog_lines = re.findall(r'^    (\w+) "([^"]*)"', content, re.MULTILINE)
    untranslated = 0
    for prefix, text in dialog_lines:
        # Skip if it's just punctuation/ellipsis or has Thai
        if any("\u0e00" <= c <= "\u0e7f" for c in text):
            continue
        if text.strip() in ("…", "...", "", "."):
            continue
        # Check if it's mostly English (has english words)
        eng_words = len(re.findall(r'[a-zA-Z]{3,}', text))
        if eng_words > 2:
            untranslated += 1

    status = "TRANSLATED" if untranslated == 0 else f"NEEDS WORK ({untranslated} left)"
    print(f"{fn:<40} {sz:>8} {blocks:>7} {'YES' if has_thai else 'NO':>10} {status:>15}")
