import os, struct

# Parse Recycle Bin $I files to find deleted files
recycle_bins = [r"\\?\C:\$Recycle.Bin", r"\\?\X:\$Recycle.Bin"]

for rb in recycle_bins:
    print(f"\n=== {rb} ===")
    try:
        for sid in os.listdir(rb):
            sid_path = os.path.join(rb, sid)
            if not os.path.isdir(sid_path):
                continue
            for fn in os.listdir(sid_path):
                if fn.startswith("$I"):
                    full = os.path.join(sid_path, fn)
                    try:
                        with open(full, "rb") as f:
                            data = f.read()
                        # $I format: header (8 bytes) = version, size (8 bytes), timestamp (8 bytes), name length (4 bytes), name (unicode)
                        if len(data) < 28:
                            continue
                        ver = struct.unpack("<Q", data[0:8])[0]
                        size = struct.unpack("<Q", data[8:16])[0]
                        name_len = struct.unpack("<I", data[24:28])[0]
                        name = data[28:28+name_len*2].decode("utf-16-le", errors="replace")
                        print(f"  $I file: {fn}")
                        print(f"    original: {name}")
                        print(f"    size: {size}")
                    except Exception as e:
                        print(f"  err {fn}: {e}")
                elif fn.startswith("$R") and fn.endswith((".rpy", ".rpy.bak")):
                    full = os.path.join(sid_path, fn)
                    sz = os.path.getsize(full)
                    print(f"  $R file: {fn} size={sz}")
    except Exception as e:
        print(f"  err: {e}")
