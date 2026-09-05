import os, re, sys
sys.stdout.reconfigure(encoding='utf-8')

base = r"X:\14DaysWithYou-5.5-pc\game\tl\thai"

stats = {"total_files": 0, "total_blocks": 0, "translated": 0, "english_left": 0, "empty_files": 0}
issues = []

for root, dirs, files in os.walk(base):
    for fn in sorted(files):
        if not fn.endswith(".rpy"):
            continue
        path = os.path.join(root, fn)
        sz = os.path.getsize(path)
        rel = os.path.relpath(path, base)
        stats["total_files"] += 1
        if sz == 0:
            stats["empty_files"] += 1
            issues.append(f"EMPTY: {rel}")
            continue
        with open(path, "r", encoding="utf-8") as f:
            content = f.read()
        # Count translate blocks
        blocks = re.findall(r'^translate thai \S+:', content, re.MULTILINE)
        stats["total_blocks"] += len(blocks)
        # Check for English dialog lines (indented, with prefix + quote)
        for i, line in enumerate(content.split("\n"), 1):
            m = re.match(r'^    (\w+) "(.*)"$', line)
            if m:
                prefix = m.group(1)
                text = m.group(2)
                if prefix in ("old",):
                    continue  # old lines should be English
                has_thai = any('\u0e00' <= c <= '\u0e7f' for c in text)
                has_english = bool(re.search(r'[A-Za-z]{4,}', text))
                # Skip if it's just variables/proper nouns
                if has_english and not has_thai:
                    # Check if it's glitch text
                    if "{glitch" in text:
                        continue
                    # Check if it's just a variable like [ch_moth]?
                    cleaned = re.sub(r'\[[^\]]+\]', '', text)
                    cleaned = re.sub(r'\{[^}]+\}', '', cleaned)
                    cleaned = cleaned.strip()
                    if not cleaned or not re.search(r'[A-Za-z]{4,}', cleaned):
                        continue
                    stats["english_left"] += 1
                    if len(issues) < 50:
                        issues.append(f"EN: {rel}:{i} [{prefix}] {text[:80]}")

print(f"Files: {stats['total_files']}")
print(f"Blocks: {stats['total_blocks']}")
print(f"Empty files: {stats['empty_files']}")
print(f"English dialog lines remaining: {stats['english_left']}")
print()
if issues:
    print("ISSUES:")
    for iss in issues:
        print(f"  {iss}")
else:
    print("No issues found!")
