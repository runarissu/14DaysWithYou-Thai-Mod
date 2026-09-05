import os, re, sys
sys.stdout.reconfigure(encoding='utf-8')

base = r"X:\14DaysWithYou-5.5-pc\game\tl\thai"
skip_dirs = []  # check all

issues = []
total_blocks = 0

for root, dirs, files in os.walk(base):
    for fn in sorted(files):
        if not fn.endswith(".rpy"):
            continue
        path = os.path.join(root, fn)
        rel = os.path.relpath(path, base)
        # Skip common.rpy (engine UI)
        if fn == "common.rpy":
            continue
        with open(path, "r", encoding="utf-8") as f:
            content = f.read()
        blocks = re.findall(r'^translate thai \S+:', content, re.MULTILINE)
        total_blocks += len(blocks)
        for i, line in enumerate(content.split("\n"), 1):
            m = re.match(r'^    (\w+) "(.*)"$', line)
            if m:
                prefix = m.group(1)
                text = m.group(2)
                if prefix == "old":
                    continue
                has_thai = any('\u0e00' <= c <= '\u0e7f' for c in text)
                has_english = bool(re.search(r'[A-Za-z]{4,}', text))
                if has_english and not has_thai:
                    if "{glitch" in text:
                        continue
                    cleaned = re.sub(r'\[[^\]]+\]', '', text)
                    cleaned = re.sub(r'\{[^}]+\}', '', cleaned)
                    cleaned = cleaned.strip()
                    if not cleaned or not re.search(r'[A-Za-z]{4,}', cleaned):
                        continue
                    issues.append(f"EN: {rel}:{i} [{prefix}] {text[:100]}")

print(f"Game script blocks: {total_blocks}")
print(f"English dialog lines remaining: {len(issues)}")
print()
if issues:
    print("ISSUES:")
    for iss in issues:
        print(f"  {iss}")
else:
    print("All game script dialog lines translated!")
