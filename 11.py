# This is not the proper solution,
# I just wanted to practice monte-carlo simulation 
# so I wrote it this way.

from random import sample, choice
from collections import Counter

P = Counter()  # history of past moves
# Puzzle input is represented in a list: [e,pm,pg,rm,rg,em,sg,...]
# the first element is elevator position, the rest is position of items


def run():
    global INIT, P, W
    f = INIT.copy()
    l = len(INIT)
    moves = 0
    while True:
        if 0 < W[-1] < moves:  # if it is past W it must start again
            f = INIT.copy()
            moves = 0
        t = choice([-1, 1])
        if (f[0] == 1 and t == -1) or (f[0] == 4 and t == 1):
            continue
        # choose 2 items from things on that floor, including E
        s = sample([i for i in range(l) if f[i] == f[0]], 2)
        # check if a gen and incompatible chip are chosen:
        compatible = True
        for gen in range(2, l, 2):
            if gen in s and any([i in s for i in range(1, l, 2) if i != gen - 1]):
                compatible = False
        if not compatible:
            continue
        nxtpos = f.copy()
        dummy = f.copy()
        nxtpos[0] += t  # move elevator
        for item in s:
            if item != 0:  # move other things
                nxtpos[item] += t
                dummy[item] = 0  # remove item from f for future checks
        # check if resulting position is valid
        valid = True
        for chip in range(1, l, 2):
            if nxtpos[chip + 1] != nxtpos[chip] and any(
                [nxtpos[gen] == nxtpos[chip] for gen in range(2, l, 2) if gen != chip + 1]
            ):
                valid = False
            if dummy[chip + 1] != dummy[chip] and any(
                [dummy[gen] == dummy[chip] for gen in range(2, l, 2) if gen != chip + 1]
            ):
                valid = False
        if not valid:
            continue
        else:  # valid move here:
            moves += 1
            f = nxtpos
            if 0 < P[tuple(f)] <= moves:
                moves = P[tuple(f)]
            else:
                P[tuple(f)] = moves
        if f == [4] * l:
            W.append(moves)
            return moves


print("Starting Part 1:")
INIT = [1, 1, 1, 1, 1, 2, 2, 3, 3, 3, 3]  # part 1 puzzle input
P.clear()
W = [0]
while True:
    k = run()
    print(f"Solved in {k} moves.")
    if W[-8:] == [k] * 8:
        break
print("Part 1: ", k, "\n\n")

print("Starting Part 2:")
INIT = [1, 1, 1, 1, 1, 2, 2, 3, 3, 3, 3, 1, 1, 1, 1]  # two more pairs on floor 1
P.clear()
W = [0]
while True:
    k = run()
    print(f"Solved in {k} moves.")
    if W[-8:] == [k] * 8:
        break
print("Part 2: ", k)
