import os, re, sys
sys.stdout.reconfigure(encoding='utf-8')

thai_dir = r"X:\14DaysWithYou-5.5-pc\game\tl\thai"

# Find all "new" lines that are identical to "old" lines (untranslated)
untranslated = []
for root, dirs, files in os.walk(thai_dir):
    for fname in files:
        if not fname.endswith(".rpy"):
            continue
        fpath = os.path.join(root, fname)
        relpath = os.path.relpath(fpath, thai_dir)
        with open(fpath, "r", encoding="utf-8") as f:
            lines = f.readlines()
        i = 0
        while i < len(lines) - 1:
            old_m = re.match(r'^\s+old "(.+)"\s*$', lines[i])
            if old_m:
                old_str = old_m.group(1)
                # Find the next "new" line
                if i + 1 < len(lines):
                    new_m = re.match(r'^\s+new "(.+)"\s*$', lines[i+1])
                    if new_m:
                        new_str = new_m.group(1)
                        if old_str == new_str:
                            # Skip if it's a proper name, keyboard key, or technical label
                            skip_words = ["14 Days With You", "English", "Language",
                                        "ENTER", "SPACE", "CTRL", "SHIFT", "TAB",
                                        "Page Up", "Page Down", "Start", "Guide",
                                        "D-Pad", "Back", "Ren'Py"]
                            if not any(w in old_str for w in skip_words):
                                untranslated.append((relpath, i+1, old_str))
                i += 2
            else:
                i += 1

print(f"Untranslated strings (new == old): {len(untranslated)}")
for relpath, line, s in untranslated[:50]:
    print(f"  {relpath}:{line} {s[:60]}")
if len(untranslated) > 50:
    print(f"  ... and {len(untranslated) - 50} more")
