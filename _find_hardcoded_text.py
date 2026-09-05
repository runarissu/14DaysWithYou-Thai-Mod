"""Find hardcoded text in screens that doesn't use _() for translation."""
import os, re, sys
sys.stdout.reconfigure(encoding='utf-8')

extracted = r"X:\14DaysWithYou-5.5-pc\_extracted\scripts"

# Find text "..." lines in screens that don't use _()
results = []
current_screen = None
in_screen = False
brace_depth = 0

for root, dirs, files in os.walk(extracted):
    for fname in files:
        if not fname.endswith(".rpy"):
            continue
        fpath = os.path.join(root, fname)
        relpath = os.path.relpath(fpath, extracted)
        with open(fpath, "r", encoding="utf-8") as f:
            for i, line in enumerate(f, 1):
                stripped = line.strip()
                # Track screen definition
                m = re.match(r'^screen\s+(\w+)\s*\(', stripped)
                if m:
                    current_screen = m.group(1)
                    in_screen = True
                    brace_depth = 0
                # Find text "..." that doesn't use _()
                # Match: text "something" or text "something":
                tm = re.match(r'^text\s+"([^"]+)"', stripped)
                if tm and current_screen:
                    text = tm.group(1)
                    # Skip if it's just variables/tags
                    clean = re.sub(r'\{[^}]+\}', '', text)
                    clean = re.sub(r'\[[^\]]+\]', '', clean).strip()
                    if not clean:
                        continue
                    # Check if it has English letters
                    has_english = any(c.isalpha() and c.isascii() for c in clean)
                    if has_english and len(clean) > 3:
                        results.append((relpath, current_screen, i, text[:100]))

print(f"Hardcoded screen text (no _()): {len(results)}")
for relpath, screen, line, text in results:
    print(f"  {relpath}:{line} [{screen}] \"{text}\"")
