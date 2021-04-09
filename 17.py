from hashlib import md5

P = b"gdjjyniy"  # Puzzle input

ToGo = [(0, 0, "")]  # (x,y, path-so-far)
Been = list()
while len(ToGo) > 0:
    point = ToGo.pop()
    if (point[0], point[1]) == (3, 3):
        Been.append(point[2])
        continue  # Path ends at the vault
    h = md5(P + point[2].encode("utf-8")).hexdigest()[:4]
    points = list()
    if h[0] in "bcdef" and 0 < point[1]:  # U is open and not walled
        points.append((point[0], point[1] - 1, point[2] + "U"))
    if h[1] in "bcdef" and point[1] < 3:  # D is open and not walled
        points.append((point[0], point[1] + 1, point[2] + "D"))
    if h[2] in "bcdef" and 0 < point[0]:  # L is open and not walled
        points.append((point[0] - 1, point[1], point[2] + "L"))
    if h[3] in "bcdef" and point[0] < 3:  # R is open and not walled
        points.append((point[0] + 1, point[1], point[2] + "R"))
    ToGo = ToGo + points

print("Part 1: ", min(Been, key=lambda x: len(x)))
print("Part 2: ", len(max(Been, key=lambda x: len(x))))