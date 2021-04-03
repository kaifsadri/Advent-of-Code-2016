from collections import Counter

L = [line.strip() for line in open("06.txt").readlines()]

i = 0
p1 = ""
p2 = ""
while True:
    try:
        chars = Counter(l[i] for l in L)
        p1 += max(chars.items(), key=lambda x: x[1])[0]
        p2 += min(chars.items(), key=lambda x: x[1])[0]
        i += 1
    except IndexError:
        break
print("Part 1: ", p1)
print("Part 2: ", p2)