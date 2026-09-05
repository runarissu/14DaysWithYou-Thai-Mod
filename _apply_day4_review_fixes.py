import os, re, sys
sys.stdout.reconfigure(encoding='utf-8')

# Apply confirmed review fixes for Day 4 parts 10-17
# Only applying clear typos, wrong words, and obvious errors
# Skipping subjective style preferences

fixes = {
    # day 4 - part 10.rpy
    "day 4 - part 10.rpy": [
        ("มาดิ๋", "มาอย่างดี"),  # typo - not a real word
        ("ไม่จำได้ว่า", "จำไม่ได้ว่า"),  # grammar
        ("ปรี่มุมมอง", "เอียงมุม"),  # wrong word
        ("ตลาดชีวิต", "ตลอดชีวิต"),  # typo
    ],
    # day 4 - part 11.rpy
    "day 4 - part 11.rpy": [
        ("ถอยกลับไปก้านหนึ่ง", "ถอยกลับไปก้าวหนึ่ง"),  # typo ก้าน→ก้าว
        ("สะดุ้กให้ตื่น", "สะดุ้งให้ตื่น"),  # typo
    ],
    # day 4 - part 12.rpy
    "day 4 - part 12.rpy": [
        ("ท่อระบายอย่าง", "ท่อระบายอากาศ"),  # typo
        ("เอียดคอ", "เอียงคอ"),  # typo
        ("ที่ไลก", "ที่ไกล"),  # typo
    ],
    # day 4 - part 13.rpy
    "day 4 - part 13.rpy": [
        ("พัสดุ์", "พัสดุ"),  # spelling
    ],
    # day 4 - part 15.rpy
    "day 4 - part 15.rpy": [
        ("บ้าเอาของแน่ๆ", "บ้าไปแล้วแน่ๆ"),  # unnatural
    ],
    # day 4 - part 16.rpy
    "day 4 - part 16.rpy": [
        ("อย่างไม่commit", "อย่างลังเล"),  # English in Thai
        ("จะreactแบบนี้", "จะตอบสนองแบบนี้"),  # English in Thai
        ("โอบแข้งขึ้นบ่า", "โอบแขนขึ้นบ่า"),  # typo แข้ง→แขน
        ("พิพิธธรรมชาติวิทยา", "พิพิธภัณฑ์สัตว์น้ำ"),  # wrong word
        ("ขอรสประหลาด", "ขายรสประหลาด"),  # typo ขอ→ขาย
    ],
    # day 4 - part 17.rpy
    "day 4 - part 17.rpy": [
        ("บองสังหรณ์", "สัญชาตญาณบอก"),  # typo
        ("สตอลเกอร์", "สตอล์กเกอร์"),  # spelling
        ("เรียกเต้นหัวใจที่เร็ว", "เรียกหัวใจที่เต้นเร็ว"),  # grammar
        ("ตัดสินความคิด", "ตัดสายความคิด"),  # wrong word
    ],
}

base_dir = r"X:\14DaysWithYou-5.5-pc\game\tl\thai\scripts\days"
total_applied = 0
total_skipped = 0

for fname, replacements in fixes.items():
    fpath = os.path.join(base_dir, fname)
    if not os.path.isfile(fpath):
        print(f"SKIP (not found): {fname}")
        continue
    with open(fpath, "r", encoding="utf-8") as f:
        content = f.read()

    file_applied = 0
    for old, new in replacements:
        if old in content:
            content = content.replace(old, new)
            file_applied += 1
            print(f"  {fname}: '{old}' -> '{new}'")
        else:
            total_skipped += 1
            print(f"  {fname}: SKIP '{old}' (not found)")

    if file_applied > 0:
        with open(fpath, "w", encoding="utf-8") as f:
            f.write(content)

    total_applied += file_applied

print(f"\nTotal applied: {total_applied}")
print(f"Total skipped: {total_skipped}")
