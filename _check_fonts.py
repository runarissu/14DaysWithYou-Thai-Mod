import os, re, sys
sys.stdout.reconfigure(encoding='utf-8')

extracted = r"X:\14DaysWithYou-5.5-pc\_extracted\scripts"

# Collect all unique font references
fonts = set()
for root, dirs, files in os.walk(extracted):
    for fname in files:
        if not fname.endswith(".rpy"):
            continue
        fpath = os.path.join(root, fname)
        with open(fpath, "r", encoding="utf-8") as f:
            for line in f:
                for m in re.finditer(r'font "fonts/([^"]+)"', line):
                    fonts.add(m.group(1))

print("All fonts referenced in game scripts:")
for f in sorted(fonts):
    print(f"  {f}")

# Check which are in replace_font.rpy
replace_path = r"X:\14DaysWithYou-5.5-pc\game\tl\thai\replace_font.rpy"
with open(replace_path, "r", encoding="utf-8") as f:
    replace_content = f.read()

print("\nFont replacement status:")
for f in sorted(fonts):
    if f'fonts/{f}' in replace_content:
        print(f"  ✓ {f}")
    else:
        print(f"  ✗ {f} -- NOT MAPPED")
