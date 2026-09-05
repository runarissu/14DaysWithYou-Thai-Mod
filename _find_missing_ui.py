"""Find UI text in screens.rpy that uses _() but might not have Thai translations."""
import os, re, sys
sys.stdout.reconfigure(encoding='utf-8')

# Check the original game screens for _() strings
extracted = r"X:\14DaysWithYou-5.5-pc\_extracted\scripts"

# Collect all _() strings from game scripts
ui_strings = set()
for root, dirs, files in os.walk(extracted):
    for fname in files:
        if not fname.endswith(".rpy"):
            continue
        fpath = os.path.join(root, fname)
        with open(fpath, "r", encoding="utf-8") as f:
            for line in f:
                for m in re.finditer(r'_\("([^"]+)"\)', line):
                    ui_strings.add(m.group(1))

# Now check which ones have Thai translations
thai_dir = r"X:\14DaysWithYou-5.5-pc\game\tl\thai"
translated = set()
for root, dirs, files in os.walk(thai_dir):
    for fname in files:
        if not fname.endswith(".rpy"):
            continue
        fpath = os.path.join(root, fname)
        with open(fpath, "r", encoding="utf-8") as f:
            for line in f:
                m = re.match(r'^\s+old "(.+)"\s*$', line)
                if m:
                    translated.add(m.group(1))

# Find untranslated
missing = ui_strings - translated
print(f"Total _() strings in game: {len(ui_strings)}")
print(f"Translated: {len(ui_strings & translated)}")
print(f"Missing translations: {len(missing)}")
for s in sorted(missing):
    print(f"  \"{s}\"")
