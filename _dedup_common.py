"""Remove duplicate string translations from common.rpy that already exist in scripts/common/."""
import sys, re, os
sys.stdout.reconfigure(encoding='utf-8')

thai_dir = r"X:\14DaysWithYou-5.5-pc\game\tl\thai"

# Collect all "old" strings from scripts/common/
scripts_common_dir = os.path.join(thai_dir, "scripts", "common")
existing_olds = set()
for fname in os.listdir(scripts_common_dir):
    if not fname.endswith(".rpy"):
        continue
    fpath = os.path.join(scripts_common_dir, fname)
    with open(fpath, "r", encoding="utf-8") as f:
        for line in f:
            m = re.match(r'^\s+old "(.+)"\s*$', line)
            if m:
                existing_olds.add(m.group(1))

print(f"Found {len(existing_olds)} old strings in scripts/common/")

# Now process common.rpy — remove blocks whose "old" is already in scripts/common/
common_path = os.path.join(thai_dir, "common.rpy")
with open(common_path, "r", encoding="utf-8") as f:
    lines = f.readlines()

new_lines = []
skip_block = False
removed = 0
kept = 0

i = 0
while i < len(lines):
    line = lines[i]
    # Check if this is an "old" line
    m = re.match(r'^(\s+)old "(.+)"\s*$', line)
    if m:
        old_str = m.group(2)
        if old_str in existing_olds:
            # Skip this old line and the next new line
            removed += 1
            # Also skip preceding comment line if any
            if new_lines and new_lines[-1].strip().startswith("#") and not new_lines[-1].strip().startswith("##"):
                new_lines.pop()
            # Skip the "new" line that follows
            if i + 1 < len(lines) and re.match(r'^\s+new "', lines[i+1]):
                i += 2
            else:
                i += 1
            # Skip blank line after
            if i < len(lines) and lines[i].strip() == "":
                i += 1
            continue
        else:
            kept += 1
    new_lines.append(line)
    i += 1

with open(common_path, "w", encoding="utf-8") as f:
    f.writelines(new_lines)

print(f"Removed: {removed} duplicates")
print(f"Kept: {kept} unique strings")
print(f"Lines: {len(new_lines)}")
