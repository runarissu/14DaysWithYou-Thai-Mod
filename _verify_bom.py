with open(r"X:\14DaysWithYou-5.5-pc\game\tl\thai\scripts\days\day 1 - meet.rpy", "rb") as f:
    d = f.read()
print("BOM count:", d.count(b"\xef\xbb\xbf"))
print("TODO count:", d.count(b"# TODO:"))
