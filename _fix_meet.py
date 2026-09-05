import sys
sys.stdout.reconfigure(encoding='utf-8')

path = r"X:\14DaysWithYou-5.5-pc\game\tl\thai\scripts\days\day 1 - meet.rpy"

with open(path, "r", encoding="utf-8") as f:
    content = f.read()

# Remove BOM characters
content = content.replace("\ufeff", "")

# Remove duplicate "# TODO: Translation updated" lines (keep only the first one)
lines = content.split("\n")
new_lines = []
seen_todo = False
for i, line in enumerate(lines):
    if line.startswith("# TODO: Translation updated"):
        if seen_todo:
            # Skip this duplicate header and the blank line after it
            continue
        seen_todo = True
    new_lines.append(line)

# Also remove any blank lines that were left behind by skipping
# Clean up: remove consecutive blank lines (max 2)
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

with open(path, "w", encoding="utf-8") as f:
    f.write("\n".join(final))

print(f"Fixed: removed BOM and duplicate TODO headers")
print(f"Lines: {len(final)}")
