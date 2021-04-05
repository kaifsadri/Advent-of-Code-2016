# Puzzle input was 1362, target (31,39)
def isopenspace(p):
    x, y = p[0], p[1]
    if x < 0 or y < 0:
        return False
    return bin(x * x + 3 * x + 2 * x * y + y + y * y + 1362).count("1") % 2 == 0


ToGo = [(1, 1, 0)]
Been = dict()

while len(ToGo) > 0:
    point = ToGo.pop()
    Been[(point[0], point[1])] = point[2]
    for d in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
        newpoint = (point[0] + d[0], point[1] + d[1])
        if isopenspace(newpoint) and (newpoint not in Been or Been[newpoint] > point[2] + 1):
            ToGo.append((newpoint[0], newpoint[1], point[2] + 1))


print(f"Part 1: {Been[(31,39)]}")
print(f"Part 2: {len({i for i in Been if Been[i] <= 50})}")
