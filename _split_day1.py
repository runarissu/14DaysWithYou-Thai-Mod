import re, os

src = r"X:\14DaysWithYou-5.5-pc\_backup_days_original\day 1.rpy"
dst_dir = r"X:\14DaysWithYou-5.5-pc\game\tl\thai\scripts\days"

with open(src, "r", encoding="utf-8") as f:
    content = f.read()
    lines = content.split("\n")

# Map label group prefix -> output filename
# Order matters: we process blocks sequentially
group_to_file = {
    "day1": "day 1 - part 01.rpy",
    "day1_meetviolet": "day 1 - meet.rpy",
    "day1_meetelanor": "day 1 - meet.rpy",
    "day1_meetren": "day 1 - meet.rpy",
    "day1_meetconan": "day 1 - meet.rpy",
    "day1_meetjaeleon": "day 1 - meet.rpy",
    "meet_jaeleon": "day 1 - meet.rpy",
    "day1_inviteren": "day 1 - part 02.rpy",
    "reninterrupt": "day 1 - reninterrupt.rpy",
    "day1_textren": "day 1 - part 03.rpy",
    "day1_callren": "day 1 - part 04.rpy",
    "sleeping": "day 1 - sleeping.rpy",
    "sleepingfloor": "day 1 - sleepingfloor.rpy",
    "sleepingbed": "day 1 - sleepingbed.rpy",
    "saygoodnight": "day 1 - saygoodnight.rpy",
    "saynothing": "day 1 - saynothing.rpy",
    "nowahoo": "day 1 - nowahoo.rpy",
    "mothaltintro": "day 1 - mothaltintro.rpy",
    "mothaltending": "day 1 - mothaltending.rpy",
    "day1_deadendstart": "day 1 - part 05.rpy",
    "day1_rejectren": "day 1 - part 05.rpy",
    "strings": "day 1 - strings.rpy",
}

# Parse blocks: each block starts with optional comments, then "translate thai LABEL:"
# and continues until the next "translate thai" or end of file
blocks = []
current_block = []
current_label = None

for line in lines:
    m = re.match(r"^translate thai (\w+):", line)
    if m:
        if current_block and current_label:
            blocks.append((current_label, current_block))
        current_label = m.group(1)
        current_block = [line]
    else:
        if current_label is not None:
            current_block.append(line)
        else:
            # header before first block
            current_block = current_block  # just skip

if current_block and current_label:
    blocks.append((current_label, current_block))

print(f"Parsed {len(blocks)} blocks")

# Group blocks by output file
file_blocks = {}
header_lines = []
# Capture header (everything before first translate thai)
for line in lines:
    if re.match(r"^translate thai ", line):
        break
    header_lines.append(line)

for label, block in blocks:
    prefix = re.sub(r"_[a-f0-9]+$", "", label)
    # find matching file
    fname = None
    # try exact prefix match first
    if prefix in group_to_file:
        fname = group_to_file[prefix]
    else:
        # try progressively shorter prefixes
        for key in group_to_file:
            if prefix.startswith(key) or label.startswith(key):
                fname = group_to_file[key]
                break
    if fname is None:
        print(f"WARNING: no file for label {label} (prefix {prefix})")
        continue
    file_blocks.setdefault(fname, []).append((label, block))

# Write files
for fname, blist in file_blocks.items():
    out_path = os.path.join(dst_dir, fname)
    with open(out_path, "w", encoding="utf-8") as f:
        # write header
        for h in header_lines:
            f.write(h + "\n")
        for label, block in blist:
            for line in block:
                f.write(line + "\n")
    sz = os.path.getsize(out_path)
    print(f"  {fname}: {len(blist)} blocks, {sz} bytes")

# Also create empty files for any missing ones
expected_files = set(group_to_file.values())
for fname in expected_files:
    out_path = os.path.join(dst_dir, fname)
    if not os.path.exists(out_path) or os.path.getsize(out_path) == 0:
        if fname not in file_blocks:
            with open(out_path, "w", encoding="utf-8") as f:
                for h in header_lines:
                    f.write(h + "\n")
            print(f"  {fname}: EMPTY (no blocks assigned)")

print(f"\nTotal files: {len(file_blocks)}")
print(f"Total blocks written: {sum(len(b) for b in file_blocks.values())}")
