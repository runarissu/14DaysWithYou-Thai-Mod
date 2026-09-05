import os, json

hist_root = r"C:\Users\lunas\AppData\Roaming\Windsurf\User\History"
sample_count = 0
thai_related = []

for d in os.listdir(hist_root):
    fp = os.path.join(hist_root, d)
    if not os.path.isdir(fp):
        continue
    entries = os.path.join(fp, "entries.json")
    if not os.path.isfile(entries):
        continue
    try:
        with open(entries, "r", encoding="utf-8", errors="replace") as f:
            data = json.load(f)
    except Exception:
        continue
    # try multiple shapes
    resource = ""
    if isinstance(data, dict):
        resource = data.get("resource") or data.get("path") or ""
        if not resource and "entries" in data:
            ent = data["entries"]
            if isinstance(ent, list) and ent:
                resource = ent[0].get("resource") or ent[0].get("path") or ""
            elif isinstance(ent, dict):
                resource = ent.get("resource") or ent.get("path") or ""
    if sample_count < 3:
        print("SAMPLE entries.json:", os.path.basename(fp))
        print("  keys:", list(data.keys()) if isinstance(data, dict) else type(data))
        print("  resource:", resource)
        sample_count += 1
    if resource:
        low = resource.lower().replace("\\", "/")
        if "thai" in low or "14days" in low or "14dayswithyou" in low:
            # find biggest version file
            versions = []
            for f in os.listdir(fp):
                full = os.path.join(fp, f)
                if os.path.isfile(full) and f != "entries.json":
                    try:
                        sz = os.path.getsize(full)
                        mt = os.path.getmtime(full)
                        versions.append((mt, sz, full))
                    except Exception:
                        pass
            versions.sort(reverse=True)
            latest_sz = versions[0][1] if versions else 0
            latest_path = versions[0][2] if versions else ""
            thai_related.append((resource, latest_sz, latest_path, len(versions)))

print(f"\nThai/14days related: {len(thai_related)}")
for r, sz, p, n in sorted(thai_related, key=lambda x: x[0])[:50]:
    print(f"  v={n} sz={sz}  {r}")
    print(f"      -> {p}")
