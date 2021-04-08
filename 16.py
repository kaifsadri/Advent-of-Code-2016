def run(part, N):
    L = "10010000000110000"  # puzzle input
    while len(L) < N:
        b = L[::-1]
        L = L + "0" + b.replace("1", "x").replace("0", "1").replace("x", "0")
    L = L[:N]
    while len(L) % 2 == 0:
        L = "".join(["1" if L[i] == L[i + 1] else "0" for i in range(0, len(L), 2)])
    return L


print("Part 1: ", run(1, 272))
print("Part 2: ", run(2, 35651584))
