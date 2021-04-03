L = open("09.txt").readline().strip()


def decomp(st, part):
    if "(" not in st:
        return len(st)
    else:
        p1 = st.find("(", 0)
        p2 = st.find(")", p1)
        numch, mult = map(lambda x: int(x), st[p1 + 1 : p2].split("x"))
        if part == 1:
            return p1 + mult * numch + decomp(st[p2 + 1 + numch :], 1)
        elif part == 2:
            return (
                p1 + mult * decomp(st[p2 + 1 : p2 + 1 + numch], 2) + decomp(st[p2 + 1 + numch :], 2)
            )


print("Part 1: ", decomp(L, 1))
print("Part 2: ", decomp(L, 2))
