L = [line.strip() for line in open("08.txt").readlines()]

G = [[0] * 50 for i in range(6)]
for line in L:
    t = line.split(" ")
    if t[0] == "rect":
        a, b = map(lambda x: int(x), t[1].split("x"))
        for col in range(a):
            for row in range(b):
                G[row][col] = 1
    elif t[1] == "row":
        r = int(t[2].split("=")[1])
        n = int(t[-1])
        for i in range(n):
            G[r].insert(0, G[r].pop())
    elif t[1] == "column":
        c = int(t[2].split("=")[1])
        n = int(t[-1])
        col = [row[c] for row in G]
        for i in range(n):
            col.insert(0, col.pop())
        for i in range(6):
            G[i][c] = col[i]

# Part 1:
print("Part 1: ", sum(i.count(1) for i in G))

# Part 2:
print("Part 2:")
for line in G:
    print("".join(map(lambda x: "█" if x == 1 else " ", line)))
