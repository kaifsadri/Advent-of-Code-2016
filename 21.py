L = [line.strip() for line in open("21.txt").readlines()]
P = list("abcdefgh")  # part 1 input
for line in L:
    t = line.split()
    ins = t[0] + t[1]
    if ins == "swapposition":
        a = P[int(t[2])]
        b = P[int(t[5])]
        P[int(t[5])] = a
        P[int(t[2])] = b
    elif ins == "swapletter":
        a, b = t[2], t[5]
        P = list("".join(P).replace(a, "0").replace(b, a).replace("0", b))
    elif ins == "reversepositions":
        P = (
            P[: int(t[2])]
            + list(reversed(P[int(t[2]) : int(t[4]) + 1]))
            + (P[int(t[4]) + 1 :] if int(t[4]) < len(P) else [])
        )
    elif ins == "moveposition":
        P.insert(int(t[5]), P.pop(int(t[2])))
    elif ins == "rotateleft":
        for i in range(int(t[2])):
            P.append(P.pop(0))
    elif ins == "rotateright":
        for i in range(int(t[2])):
            P.insert(0, P.pop())
    elif ins == "rotatebased":
        l = P.index(t[-1])
        if l >= 4:
            l += 1
        for i in range(l + 1):
            P.insert(0, P.pop())
print("Part 1: ", "".join(P))

P = list("fbgdceah")  # part 2 input
for line in L[::-1]:
    t = line.split()
    ins = t[0] + t[1]
    if ins == "swapposition":
        a = P[int(t[2])]
        b = P[int(t[5])]
        P[int(t[5])] = a
        P[int(t[2])] = b
    elif ins == "swapletter":
        a, b = t[2], t[5]
        P = list("".join(P).replace(a, "0").replace(b, a).replace("0", b))
    elif ins == "reversepositions":
        P = (
            P[: int(t[2])]
            + list(reversed(P[int(t[2]) : int(t[4]) + 1]))
            + (P[int(t[4]) + 1 :] if int(t[4]) < len(P) else [])
        )
    elif ins == "moveposition":
        P.insert(int(t[2]), P.pop(int(t[5])))
    elif ins == "rotateleft":
        for i in range(int(t[2])):
            P.insert(0, P.pop())
    elif ins == "rotateright":
        for i in range(int(t[2])):
            P.append(P.pop(0))
    elif ins == "rotatebased":
        M = {
            1: 1,
            3: 2,
            5: 3,
            7: 4,
            2: 6,
            4: 7,
            6: 0,
            0: 1,
        }  # reverse of what happened in rorate
        for i in range(M[P.index(t[-1])]):
            P.append(P.pop(0))
print("Part 2: ", "".join(P))