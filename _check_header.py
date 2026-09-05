with open(r"X:\14DaysWithYou-5.5-pc\game\thai_mod.rpa", "rb") as f:
    header = f.read(35)
    print(repr(header))
    print(f"Length: {len(header)}")
