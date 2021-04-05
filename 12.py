def run(r=[0, 0, 0, 0]):
    L = [line.strip() for line in open("12.txt").readlines()]
    R = dict(zip("abcd", r))
    pos = 0
    while pos < len(L):
        t = L[pos].split(" ")
        if t[0] == "cpy":
            if t[1].isnumeric():
                R[t[2]] = int(t[1])
            else:
                R[t[2]] = R[t[1]]
            pos += 1
        elif t[0] == "inc":
            R[t[1]] += 1
            pos += 1
        elif t[0] == "dec":
            R[t[1]] -= 1
            pos += 1
        elif t[0] == "jnz":
            if t[1].isnumeric():
                if int(t[1]) != 0:
                    pos += int(t[2])
                else:
                    pos += 1
            else:
                if R[t[1]] != 0:
                    pos += int(t[2])
                else:
                    pos += 1
    return R["a"]


print(f"Part 1: {run([0,0,0,0])}")
print(f"Part 2: {run([0,0,1,0])}")
