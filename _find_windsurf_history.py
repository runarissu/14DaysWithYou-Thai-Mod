import os, json, glob

hist_root = r"C:\Users\lunas\AppData\Roaming\Windsurf\User\History"
if not os.path.isdir(hist_root):
    print("no history dir")
    raise SystemExit

# Each subfolder is a hash; contains entries.json with resource path + versions
hits = []
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
    # entries.json usually has "resource" path and "entries" list
    resource = data.get("resource") or data.get("path") or ""
    if not resource:
        # sometimes wrapped
        ent = data.get("entries") or []
        if ent and isinstance(ent, list):
            resource = ent[0].get("resource") or ""
    if not resource:
        continue
    low = resource.lower().replace("\\", "/")
    if "day 1" in low and low.endswith(".rpy"):
        # find the latest version file
        versions = []
        for f in os.listdir(fp):
            if f.endswith(".rpy") or f.isdigit() or f.startswith("version"):
                full = os.path.join(fp, f)
                try:
                    sz = os.path.getsize(full)
                    mt = os.path.getmtime(full)
                except Exception:
                    continue
                versions.append((mt, sz, full))
        versions.sort(reverse=True)
        if versions:
            mt, sz, latest = versions[0]
            # check if it has thai content
            has_thai = False
            try:
                with open(latest, "rb") as fh:
                    raw = fh.read(4000)
                try:
                    txt = raw.decode("utf-8")
                except Exception:
                    txt = raw.decode("utf-8", errors="replace")
                # crude thai range check
                has_thai = any("\u0e00" <= c <= "\u0e7f" for c in txt)
            except Exception:
                pass
            hits.append((resource, sz, has_thai, latest, len(versions)))

hits.sort(key=lambda x: x[0])
print(f"Found {len(hits)} day 1 .rpy resources in history:")
for r, sz, thai, latest, n in hits:
    flag = "THAI" if thai else "english/empty"
    print(f"  [{flag}] versions={n} size={sz}  {r}")
    print(f"      latest: {latest}")
