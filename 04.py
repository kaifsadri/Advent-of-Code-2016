from collections import Counter

L = [line.strip() for line in open("04.txt").readlines()]

D = dict(zip("abcdefghijklmnopqrstuvwxyz", "bcdefghijklmnopqrstuvwxyza"))

n = 0
part1 = 0
part2 = 0
for l in L:
    chs = l[-6:-1]
    sec = int(l[-10:-7])
    name = l[:-10].replace("-", "")
    c = Counter(name)
    m = max(c.values())
    s = ""
    while m != 0:
        t = sorted(i for i in c if c[i] == m)
        s += "".join(t)
        m -= 1
        if s[:5] == chs:
            part1 += sec
            for i in range(sec):
                name = "".join(list(map(lambda x: D[x], name)))
            if name.startswith("north"):
                part2 = sec
            break
print("Part 1: ", part1)
print("Part 2: ", part2)
