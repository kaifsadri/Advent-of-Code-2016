from collections import deque

L = deque(
    sorted(
        [
            tuple(map(lambda x: int(x), line.strip().split("-")))
            for line in open("20.txt").readlines()
        ]
    )
)

MIN = 0
while L:
    r = L.popleft()
    if r[0] <= MIN:
        MIN = max(MIN, r[1] + 1)
    else:
        break
print("Part 1 : ", MIN)

L = deque(
    sorted(
        [
            tuple(map(lambda x: int(x), line.strip().split("-")))
            for line in open("20.txt").readlines()
        ]
    )
)

TOT = 0
while L:
    r = L.popleft()
    TOT += max(r[0] - MIN, 0)
    MIN = max(r[1] + 1, MIN)

print("Part 2 : ", TOT)