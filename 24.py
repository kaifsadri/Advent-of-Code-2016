from collections import deque
from itertools import permutations

L = [line.strip() for line in open("24.txt").readlines()]

nums = dict()
for row in range(len(L)):
    for col in range(len(L[0])):
        if L[row][col] in "01234567":
            nums[L[row][col]] = (row, col)


distances = dict()
M = [(1, 0), (0, 1), (-1, 0), (0, -1)]
for number in nums:
    togo = deque([(nums[number], 0)])
    been = dict()
    while len(togo) > 0:
        p, n = togo.popleft()
        been[p] = n
        for m in M:
            np = (p[0] + m[0], p[1] + m[1])
            if (
                0 <= np[0] < len(L)
                and 0 <= np[1] < len(L[0])
                and L[np[0]][np[1]] != "#"
                and (np not in been or been[np] > n + 1)
            ):
                togo.appendleft((np, n + 1))
    distances[number] = been


def path_len(seq):
    global nums
    s = seq[0]
    result = 0
    for point in seq[1:]:
        result += distances[s][nums[point]]
        s = point
    return result


R = 1000000
S = 1000000
for s in permutations("1234567"):
    m = path_len(["0"] + list(s))
    n = path_len(["0"] + list(s) + ["0"])
    if R > n:
        R = m
    if S > n:
        S = n
print("Part 1: ", R)
print("Part 2: ", S)