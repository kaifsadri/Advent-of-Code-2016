L = [line.strip() for line in open("02.txt").readlines()]

loc = (2, 0)
M = {"U": (-1, 0), "L": (0, -1), "D": (1, 0), "R": (0, 1)}
PAD = [[0, 0, 1, 0, 0], [0, 2, 3, 4, 0], [5, 6, 7, 8, 9], [0, "A", "B", "C", 0], [0, 0, "D", 0, 0]]

for line in L:
    for c in line:
        nl = (loc[0] + M[c][0], loc[1] + M[c][1])
        if all(nl[i] in range(5) for i in range(2)) and 0 != PAD[nl[0]][nl[1]]:
            loc = tuple(nl)
        else:
            pass
    print(PAD[loc[0]][loc[1]], end="")
print()
