import re, os

def parse_blocks(filepath):
    """Parse a .rpy file into (header, [(label, block_lines), ...])"""
    with open(filepath, "r", encoding="utf-8") as f:
        lines = f.read().split("\n")
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
    return header, blocks

def extract_range(src_file, start_after_label, end_before_label, output_file):
    """Extract blocks between start_after_label (exclusive) and end_before_label (exclusive)"""
    header, blocks = parse_blocks(src_file)

    # Find indices
    start_idx = 0
    end_idx = len(blocks)
    for i, (label, _) in enumerate(blocks):
        if label == start_after_label:
            start_idx = i + 1
        if label == end_before_label:
            end_idx = i
            break

    extracted = blocks[start_idx:end_idx]
    print(f"  Extracted {len(extracted)} blocks (indices {start_idx}-{end_idx-1})")
    print(f"  First: {extracted[0][0] if extracted else 'NONE'}")
    print(f"  Last: {extracted[-1][0] if extracted else 'NONE'}")

    # Write
    with open(output_file, "w", encoding="utf-8") as f:
        for h in header:
            f.write(h + "\n")
        for label, block in extracted:
            for line in block:
                f.write(line + "\n")

    sz = os.path.getsize(output_file)
    print(f"  Written: {output_file} ({sz} bytes)")
    return len(extracted)

dst_dir = r"X:\14DaysWithYou-5.5-pc\game\tl\thai\scripts\days"
backup_dir = r"X:\14DaysWithYou-5.5-pc\_backup_days_original"

# Day 3 part 02: between part 01 last (day3_alonemorning_ecf0768a) and part 03 first (day3_meetingkiara_ad9277ed)
print("=== Day 3 part 02 ===")
n = extract_range(
    os.path.join(backup_dir, "day 3.rpy"),
    "day3_alonemorning_ecf0768a",
    "day3_meetingkiara_ad9277ed",
    os.path.join(dst_dir, "day 3 - part 02.rpy")
)

# Day 4 part 09: between part 08 last (day4_visitren_857599f8) and part 10 first (day4_snooping_d6ce37a5)
print("\n=== Day 4 part 09 ===")
n = extract_range(
    os.path.join(backup_dir, "day 4.rpy"),
    "day4_visitren_857599f8",
    "day4_snooping_d6ce37a5",
    os.path.join(dst_dir, "day 4 - part 09.rpy")
)

# Day 5 part 05: between part 04 last (day5_changingstalls_5c62a19b) and part 06 first (day5_covescene_baec013d)
print("\n=== Day 5 part 05 ===")
n = extract_range(
    os.path.join(backup_dir, "day 5.rpy"),
    "day5_changingstalls_5c62a19b",
    "day5_covescene_baec013d",
    os.path.join(dst_dir, "day 5 - part 05.rpy")
)
