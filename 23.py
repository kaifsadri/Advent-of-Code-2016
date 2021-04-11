def run(r=[0, 0, 0, 0]):
    L = [line.strip() for line in open("23.txt").readlines()]
    R = dict(zip("abcd", r))
    pos = 0
    while pos < len(L):
        # print(R) # used in part 2
        t = L[pos].split()
        if t[0] == "cpy":
            try:
                v = int(t[1])
            except ValueError:
                v = R[t[1]]
            if not t[2].isnumeric():
                R[t[2]] = v
            pos += 1
        elif t[0] == "inc":
            R[t[1]] += 1
            pos += 1
        elif t[0] == "dec":
            R[t[1]] -= 1
            pos += 1
        elif t[0] == "jnz":
            try:
                c = int(t[1])
            except ValueError:
                c = R[t[1]]
            try:
                v = int(t[2])
            except ValueError:
                v = R[t[2]]
            if c != 0:
                pos += v
            else:
                pos += 1
        elif t[0] == "tgl":
            try:
                l = L[pos + R[t[1]]].split()
                if len(l) == 2:
                    l[0] = "dec" if l[0] == "inc" else "inc"
                elif len(l) == 3:
                    l[0] = "cpy" if l[0] == "jnz" else "jnz"
                L[pos + R[t[1]]] = " ".join(l)
            except IndexError:
                pass
            pos += 1
    return R["a"]


print(f"Part 1: {run([7,0,0,0])}")
# running part 1 in terminal with print(R) in the beginning of loop
# suggests that it caclulates a = 7!+77*79 = 11123. So:
print(f"Part 2: {12 * 11 * 10 * 9 * 8 * 7 * 6 * 5 * 4 * 3 * 2 + 79 * 77}")
