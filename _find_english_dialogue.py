"""Find dialogue lines in Thai translation files that are still in English."""
import os, re, sys
sys.stdout.reconfigure(encoding='utf-8')

thai_dir = r"X:\14DaysWithYou-5.5-pc\game\tl\thai\scripts"

# Find all translated dialogue lines (not comments, not old/new string pairs)
# Look for character dialogue: char "text" or extend "text"
# where the text contains mostly English words

english_dialogue = []
for root, dirs, files in os.walk(thai_dir):
    for fname in files:
        if not fname.endswith(".rpy"):
            continue
        fpath = os.path.join(root, fname)
        relpath = os.path.relpath(fpath, thai_dir)
        with open(fpath, "r", encoding="utf-8") as f:
            for i, line in enumerate(f, 1):
                stripped = line.strip()
                # Skip comments, empty lines, translate labels, old/new pairs
                if stripped.startswith("#") or not stripped:
                    continue
                if stripped.startswith("translate") or stripped.startswith("old ") or stripped.startswith("new "):
                    continue
                if stripped.startswith("with ") or stripped.startswith("extend"):
                    # Check extend lines too
                    pass
                # Look for dialogue: charname "text" or extend "text"
                m = re.match(r'^(?:extend\s+)?"(.+)"', stripped)
                if not m:
                    m = re.match(r'^\w+\s+"(.+)"', stripped)
                if m:
                    text = m.group(1)
                    # Remove Ren'Py tags and variables
                    clean = re.sub(r'\{[^}]+\}', '', text)
                    clean = re.sub(r'\[[^\]]+\]', '', clean)
                    # Count Thai vs Latin characters
                    thai_chars = sum(1 for c in clean if '\u0e00' <= c <= '\u0e7f')
                    latin_chars = sum(1 for c in clean if c.isalpha() and c.isascii())
                    # If no Thai chars and has Latin chars, it's untranslated
                    if thai_chars == 0 and latin_chars > 2:
                        # Skip if it's just a variable or short word
                        if len(clean.strip()) > 3:
                            english_dialogue.append((relpath, i, stripped[:100]))

print(f"Untranslated dialogue lines: {len(english_dialogue)}")
for relpath, line, text in english_dialogue[:80]:
    print(f"  {relpath}:{line} {text}")
if len(english_dialogue) > 80:
    print(f"  ... and {len(english_dialogue) - 80} more")
