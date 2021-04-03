from hashlib import md5

L = b"ugkcyxxp"  # puzzle input
i = 0
h = md5(L + str(i).encode("utf-8")).hexdigest()
P = ""
while True:
    if h[:5] == "00000":
        P += h[5]
    if len(P) == 8:
        print("Part 1: ", P)
        break
    i += 1
    h = md5(L + str(i).encode("utf-8")).hexdigest()

i = 0
h = md5(L + str(i).encode("utf-8")).hexdigest()
P = list("________")
while True:
    if h[:5] == "00000":
        if h[5].isnumeric() and 0 <= int(h[5]) <= 7 and P[int(h[5])] == "_":
            P[int(h[5])] = h[6]
    if "_" not in P:
        print("Part 2: ", "".join(P))
        break
    i += 1
    h = md5(L + str(i).encode("utf-8")).hexdigest()
