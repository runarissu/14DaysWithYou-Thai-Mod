import os, re, sys
sys.stdout.reconfigure(encoding='utf-8')

thai_dir = r"X:\14DaysWithYou-5.5-pc\game\tl\thai"

# Find untranslated strings, excluding engine-only strings
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
                if i + 1 < len(lines):
                    new_m = re.match(r'^\s+new "(.+)"\s*$', lines[i+1])
                    if new_m and new_m.group(1) == old_str:
                        # Skip engine/director/update/sync strings
                        skip = False
                        engine_patterns = [
                            "director", "Director", "transform", "Transition:",
                            "Channel:", "Audio Filename:", "Behind:",
                            "Statement:", "Tag:", "Attributes:",
                            "Customize director", "Click to",
                            "sync", "Sync", "App Store",
                            "update", "Update", "download", "Download",
                            "unpacking", "digest", "signature",
                            "Self-voicing", "Speech Bubble",
                            "Translation identifier", "translates",
                            "Copied to clipboard", "Contacting",
                            "permission", "simulated",
                            "DejaVu", "Opendyslexic",
                            "%b %d", "⬆", "⬇",
                            "(statement)", "(tag)", "(attributes)",
                            "(transform)", "(transition)", "(channel)",
                            "(filename)", "renpy", "Ren'Py",
                            "14 Days With You", "English", "Language",
                            "ENTER", "SPACE", "CTRL", "SHIFT", "TAB",
                            "Page Up", "Page Down", "Start", "Guide",
                            "D-Pad", "Back",
                        ]
                        for p in engine_patterns:
                            if p in old_str:
                                skip = True
                                break
                        if not skip and len(old_str) > 2:
                            untranslated.append((relpath, i+1, old_str))
                i += 2
            else:
                i += 1

print(f"Potentially untranslated game strings: {len(untranslated)}")
for relpath, line, s in untranslated:
    print(f"  {relpath}:{line} {s[:80]}")
