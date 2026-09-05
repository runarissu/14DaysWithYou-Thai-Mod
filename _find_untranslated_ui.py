"""Find untranslated UI strings (old/new pairs where new == old or new is English)."""
import os, re, sys
sys.stdout.reconfigure(encoding='utf-8')

thai_dir = r"X:\14DaysWithYou-5.5-pc\game\tl\thai"

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
                    if new_m:
                        new_str = new_m.group(1)
                        # Check if new has Thai chars
                        clean = re.sub(r'\{[^}]+\}', '', new_str)
                        clean = re.sub(r'\[[^\]]+\]', '', clean)
                        thai_chars = sum(1 for c in clean if '\u0e00' <= c <= '\u0e7f')
                        if thai_chars == 0 and len(clean.strip()) > 1:
                            # Skip known intentional English
                            skip = False
                            skip_words = ["14 Days With You", "English", "Language",
                                "ENTER", "SPACE", "CTRL", "SHIFT", "TAB",
                                "Page Up", "Page Down", "Start", "Guide",
                                "D-Pad", "Back", "Ren'Py", "DejaVu", "Opendyslexic",
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
                                "%b %d", "⬆", "⬇",
                                "(statement)", "(tag)", "(attributes)",
                                "(transform)", "(transition)", "(channel)",
                                "(filename)", "(clear retained bubbles)",
                                "Force GL2", "Force ANGLE2", "Force GLES2",
                                "Enable (No Blocklist)",
                                "renderer", "rendering", "graphics",
                                "log.txt", "documentation",
                                "Calibrating", "Press or move",
                                "traceback", "BBcode", "Markdown", "Discord",
                                "GL2", "ANGLE2", "GLES2",
                                "Blocklist",
                                "[u.version]",
                                "LEFT", "RIGHT", "UP", "DOWN",
                                "renpy", "Ren'Py",
                                "LEFT TRIGGER", "RIGHT SHOULDER",
                                "Left Trigger", "Right Shoulder",
                                "WE ZOOMIN",
                                "is available",
                                "This computer",
                                "This game requires",
                                "Its graphics",
                                "More details",
                                "Copies the traceback",
                                "This program contains",
                                "free software",
                                "I'm {color",
                                "Saint (cutiesai)",
                                "Yuli", "Pixabay", "Pexels", "Wattson", "Ariane",
                                "BGM", "SFX", "Nature", "Kinetic", "Discord rich",
                                "Game engine",
                                "Everything else",
                                "And a big thank you",
                                "supported the demo",
                            ]
                            for p in skip_words:
                                if p in old_str:
                                    skip = True
                                    break
                            if not skip:
                                untranslated.append((relpath, i+1, old_str[:80], new_str[:80]))
                i += 2
            else:
                i += 1

print(f"Untranslated UI strings: {len(untranslated)}")
for relpath, line, old, new in untranslated:
    print(f"  {relpath}:{line}")
    print(f"    old: {old}")
    print(f"    new: {new}")
