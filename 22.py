L = [line.strip() for line in open("22.txt").readlines()[2:]]

Nodes = dict()  # Nodes[(x,y)]=[SIZE, USED, AVAIL, USE%]
for line in L:
    t = line.split()
    loc = t[0].split("-")
    Nodes[(int(loc[1][1:]), int(loc[2][1:]))] = list(
        map(lambda x: int(x), (t[i][:-1] for i in range(1, 5)))
    )

T = 0
for node1 in Nodes:
    for node2 in Nodes:
        if node1 != node2 and Nodes[node1][1] > 0 and Nodes[node1][1] <= Nodes[node2][2]:
            T += 1
print("Part 1: ", T)

MX = max(Nodes, key=lambda t: t[0])[0]
MY = max(Nodes, key=lambda t: t[1])[1]
MS = Nodes[[item for item in Nodes if Nodes[item][1] == 0][0]][0]

for y in range(MY + 1):
    for x in range(MX + 1):
        c = "."
        if (x, y) == (0, 0):
            c = "(.)"
        elif (x, y) == (MX, 0):
            c = "G"
        elif Nodes[(x, y)][1] > MS:  # impossible nodes
            c = "#"
        elif Nodes[(x, y)][1] == 0:
            c = "_"
        print(f"{c:3} ", end="")
    print()

print("Part 2: ", 14 + 25 + 27 + 5 * 35 + 1)
