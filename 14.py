from hashlib import md5


def run(part):
    C3 = dict()
    K = set()
    i = 0
    while len(K) < 64:
        h = md5(b"ahsbgdzn" + str(i).encode("utf-8")).hexdigest()  # puzzle input = "ahsbgdzn"
        if part == 2:
            for b in range(2016):
                h = md5(h.encode("utf-8")).hexdigest()
        for x in range(len(h) - 2):
            if h[x] * 3 == h[x : x + 3]:
                C3[i] = h[x]
                break
        for x in range(len(h) - 4):
            if h[x] * 5 == h[x : x + 5]:
                for t in range(max(0, i - 1000), i):
                    if t in C3 and C3[t] == h[x]:
                        K.add(t)  # using set so t will not be double-counted
        i += 1
    return sorted(K)[63]  # sort to present the right order


print("Part 1: ", run(1))
print("Part 2: ", run(2))