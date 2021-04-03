L = [line.strip() for line in open("02.txt").readlines()]

loc = (1, 1)
M = {"U": (-1, 0), "L": (0, -1), "D": (1, 0), "R": (0, 1)}
PAD = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

for line in L:
    for c in line:
        nl = (loc[0] + M[c][0], loc[1] + M[c][1])
        if nl[0] in {0, 1, 2} and nl[1] in {0, 1, 2}:
            loc = tuple(nl)
        else:
            pass
    print(PAD[loc[0]][loc[1]], end="")
print()
