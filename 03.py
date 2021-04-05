L = [line for line in open("03.txt").readlines()]


def possible(t):
    if t[0] + t[1] <= t[2] or t[1] + t[2] <= t[0] or t[0] + t[2] <= t[1]:
        return 0
    else:
        return 1


n = 0
for line in L:
    t = list(map(lambda x: int(x), line.split()))
    n += possible(t)
print("Part 1: ", n)

col1 = list()
col2 = list()
col3 = list()
for line in L:
    t = list(map(lambda x: int(x), line.split()))
    col1.append(t[0])
    col2.append(t[1])
    col3.append(t[2])
n = 0
for i in range(0, len(col1), 3):
    n += possible(col1[i : i + 3])
    n += possible(col2[i : i + 3])
    n += possible(col3[i : i + 3])
print("Part 2: ", n)
