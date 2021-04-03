L = [line for line in open("03.txt").readlines()]


def possible(t):
    if t[0] + t[1] <= t[2] or t[1] + t[2] <= t[0] or t[0] + t[2] <= t[1]:
        return 0
    else:
        return 1


n = 0
for line in L:
    a = line[2:5]
    b = line[7:10]
    c = line[12:15]
    a = int(a.strip())
    b = int(b.strip())
    c = int(c.strip())
    n += possible([a, b, c])
print("Part 1: ", n)

col1 = list()
col2 = list()
col3 = list()
for line in L:
    a = line[2:5]
    b = line[7:10]
    c = line[12:15]
    a = int(a.strip())
    b = int(b.strip())
    c = int(c.strip())
    col1.append(a)
    col2.append(b)
    col3.append(c)
n = 0
for i in range(0, len(col1), 3):
    n += possible(col1[i : i + 3])
    n += possible(col2[i : i + 3])
    n += possible(col3[i : i + 3])
print("Part 2: ", n)
