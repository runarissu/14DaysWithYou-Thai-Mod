import re, os

src = r"X:\14DaysWithYou-5.5-pc\game\tl\thai\scripts\days\day 1 - meet.rpy"
dst_dir = r"X:\14DaysWithYou-5.5-pc\game\tl\thai\scripts\days"

with open(src, "r", encoding="utf-8") as f:
    lines = f.read().split("\n")

# Parse blocks
header = []
blocks = []
current_label = None
current_block = []
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
            header.append(line)
if current_block and current_label:
    blocks.append((current_label, current_block))

print(f"Total blocks: {len(blocks)}")

# Split into 3 parts: 0-109, 110-219, 220-329
parts = [
    ("day 1 - meet 1.rpy", blocks[0:110]),
    ("day 1 - meet 2.rpy", blocks[110:220]),
    ("day 1 - meet 3.rpy", blocks[220:]),
]

for fname, blist in parts:
    out_path = os.path.join(dst_dir, fname)
    with open(out_path, "w", encoding="utf-8") as f:
        for h in header:
            f.write(h + "\n")
        for label, block in blist:
            for line in block:
                f.write(line + "\n")
    sz = os.path.getsize(out_path)
    print(f"  {fname}: {len(blist)} blocks, {sz} bytes")
