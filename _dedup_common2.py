"""Remove ALL duplicate string translations from common.rpy that exist in any other .rpy file."""
import sys, re, os
sys.stdout.reconfigure(encoding='utf-8')

thai_dir = r"X:\14DaysWithYou-5.5-pc\game\tl\thai"
common_path = os.path.join(thai_dir, "common.rpy")

# Collect all "old" strings from ALL .rpy files EXCEPT common.rpy
existing_olds = set()
for root, dirs, files in os.walk(thai_dir):
    for fname in files:
        if not fname.endswith(".rpy"):
            continue
        fpath = os.path.join(root, fname)
        relpath = os.path.relpath(fpath, thai_dir)
        if relpath == "common.rpy":
            continue
        with open(fpath, "r", encoding="utf-8") as f:
            for line in f:
                m = re.match(r'^\s+old "(.+)"\s*$', line)
                if m:
                    existing_olds.add(m.group(1))

print(f"Found {len(existing_olds)} old strings in other files")

# Process common.rpy — remove blocks whose "old" is already elsewhere
with open(common_path, "r", encoding="utf-8") as f:
    lines = f.readlines()

new_lines = []
removed = 0
kept = 0

i = 0
while i < len(lines):
    line = lines[i]
    m = re.match(r'^(\s+)old "(.+)"\s*$', line)
    if m:
        old_str = m.group(2)
        if old_str in existing_olds:
            removed += 1
            # Remove preceding comment line if any (single #, not ##)
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

# Clean up excessive blank lines
final = []
blank_count = 0
for line in new_lines:
    if line.strip() == "":
        blank_count += 1
        if blank_count <= 2:
            final.append(line)
    else:
        blank_count = 0
        final.append(line)

with open(common_path, "w", encoding="utf-8") as f:
    f.writelines(final)

print(f"Removed: {removed} duplicates")
print(f"Kept: {kept} unique strings")
print(f"Lines: {len(final)}")
