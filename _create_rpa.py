"""
Create a Ren'Py .rpa archive (version 3.0) from a directory.
RPA v3 format:
  - Header: "RPA-3.0 " + hex(offset) + " " + hex(key) + "\n"
  - Index: pickled dict of {filename: [(offset, length, prefix), ...]}
  - File data
All offsets and lengths are XORed with the key.
"""
import os, sys, pickle, zlib

sys.stdout.reconfigure(encoding='utf-8')

def create_rpa(source_dir, output_path):
    key = 0x12345678  # arbitrary key
    files = []

    # Collect all files
    for root, dirs, fnames in os.walk(source_dir):
        for fn in sorted(fnames):
            full = os.path.join(root, fn)
            rel = os.path.relpath(full, source_dir).replace("\\", "/")
            files.append((rel, full))

    with open(output_path, "wb") as out:
        # Write placeholder header (we'll come back and fix the offset)
        header_placeholder = b"RPA-3.0 00000000000 00000000\n"
        out.write(header_placeholder)

        index = {}
        for rel, full in files:
            with open(full, "rb") as f:
                data = f.read()
            offset = out.tell()
            out.write(data)
            length = len(data)
            # XOR offset and length with key
            index[rel] = [(offset ^ key, length ^ key, b"")]

        # Write index (zlib compressed pickle)
        index_offset = out.tell()
        pickled = pickle.dumps(index, protocol=2)
        compressed = zlib.compress(pickled)
        out.write(compressed)

        # Go back and write the real header
        out.seek(0)
        header = f"RPA-3.0 {index_offset:012x} {key:08x}\n".encode("ascii")
        out.write(header)

    print(f"Created: {output_path}")
    print(f"  Files: {len(files)}")
    print(f"  Size: {os.path.getsize(output_path)} bytes")

if __name__ == "__main__":
    source = r"X:\14DaysWithYou-5.5-pc\game\tl\thai"
    output = r"X:\14DaysWithYou-5.5-pc\game\thai_mod.rpa"
    create_rpa(source, output)
