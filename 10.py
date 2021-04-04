from collections import defaultdict
from random import choice

L = [line.strip() for line in open("10.txt").readlines()]
B = defaultdict(list)
I = defaultdict(list)
O = dict()

i = 0
for line in L:
    t = line.split(" ")
    if t[0] == "value":
        B[int(t[-1])].append(int(t[1]))
    else:
        I[int(t[1])] = [" ".join([t[5], t[6]]), " ".join([t[10], t[11]])]


while True:
    bot = choice(list(B.keys()))
    if len(B[bot]) == 2:
        if 17 in B[bot] and 61 in B[bot]:
            print("Part 1: ", bot)
        if 0 in O and 1 in O and 2 in O:
            print("Part 2: ", O[0] * O[1] * O[2])
            break
        low, high = I[bot][0], I[bot][1]
        low_type, low_id = low.split(" ")
        high_type, high_id = high.split(" ")
        if low_type == "bot":
            B[int(low_id)].append(min(B[bot]))
        else:
            O[int(low_id)] = min(B[bot])

        if high_type == "bot":
            B[int(high_id)].append(max(B[bot]))
        else:
            O[int(high_id)] = max(B[bot])
        B[bot].clear()
