import re, sys, os
sys.stdout.reconfigure(encoding='utf-8')

files_to_check = [
    r"X:\14DaysWithYou-5.5-pc\game\tl\thai\scripts\days\day 1 - mothaltending.rpy",
    r"X:\14DaysWithYou-5.5-pc\game\tl\thai\scripts\days\day 1 - strings.rpy",
    r"X:\14DaysWithYou-5.5-pc\game\tl\thai\scripts\days\day 5 - part 05.rpy",
]

for path in files_to_check:
    print(f"\n=== {os.path.basename(path)} ===")
    with open(path, "r", encoding="utf-8") as f:
        lines = f.readlines()
    in_block = False
    block_label = ""
    for i, line in enumerate(lines, 1):
        s = line.rstrip("\n")
        if re.match(r'^translate thai \S+:', s):
            in_block = True
            block_label = s
            continue
        if in_block and re.match(r'^    (\w+) "', s):
            m = re.match(r'^    (\w+) "(.*)"$', s)
            if m:
                text = m.group(2)
                # Check if it looks like English (has English letters and not Thai)
                has_thai = any('\u0e00' <= c <= '\u0e7f' for c in text)
                has_english = bool(re.search(r'[A-Za-z]{3,}', text))
                if has_english and not has_thai:
                    print(f"  L{i}: {block_label}")
                    print(f"    {s.strip()}")
            in_block = False
