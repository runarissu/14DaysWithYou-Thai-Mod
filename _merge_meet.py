import sys
sys.stdout.reconfigure(encoding='utf-8')

base = r"X:\14DaysWithYou-5.5-pc\game\tl\thai\scripts\days"
files = [
    (f"{base}\\day 1 - meet 1.rpy", True),   # keep header
    (f"{base}\\day 1 - meet 2.rpy", False),  # skip header
    (f"{base}\\day 1 - meet 3.rpy", False),  # skip header
]

out_path = f"{base}\\day 1 - meet.rpy"

merged = []
for path, keep_header in files:
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()
    lines = content.split("\n")
    if not keep_header:
        # Skip the first "# TODO:" line and the blank line after it
        i = 0
        if lines and lines[0].startswith("# TODO:"):
            i = 1
            # skip blank lines after
            while i < len(lines) and lines[i].strip() == "":
                i += 1
        lines = lines[i:]
    merged.extend(lines)
    # ensure separation between files
    if merged and merged[-1].strip() != "":
        merged.append("")

with open(out_path, "w", encoding="utf-8") as f:
    f.write("\n".join(merged))

print(f"Merged -> {out_path}")
print(f"Total lines: {len(merged)}")
