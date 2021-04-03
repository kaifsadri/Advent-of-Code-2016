from regex import split

L = [line.strip() for line in open("07.txt").readlines()]


def ABBA(s):
    for i in range(0, len(s) - 3):
        if s[i] != s[i + 1] and s[i] == s[i + 3] and s[i + 1] == s[i + 2]:
            return True
    return False


def ABAs(s):
    abas = []
    for i in range(0, len(s) - 2):
        if s[i] == s[i + 2] and s[i] != s[i + 1]:
            abas.append(s[i : i + 3])
    return abas


p1 = 0
p2 = 0
for line in L[:]:
    parts = split(r"\]|\[", line)
    sups = parts[0::2]
    hyps = parts[1::2]
    if any([ABBA(s) for s in sups]) and not any([ABBA(s) for s in hyps]):
        p1 += 1
    ssl = False
    for s in sups:
        aba = ABAs(s)
        for a in aba:
            if any(a[1] + a[0] + a[1] in h for h in hyps):
                ssl = True
    if ssl:
        p2 += 1

print("Part 1: ", p1)
print("Part 2: ", p2)