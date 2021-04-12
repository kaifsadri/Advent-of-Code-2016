def run(r=[0, 0, 0, 0]):
    L = [line.strip() for line in open("25.txt").readlines()]
    R = dict(zip("abcd", r))
    pos = 0
    result = ""
    while (
        pos < len(L) and len(result) < 24
    ):  # empirically, periods of repetition are 6 and 12, so 24 will do
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
        elif t[0] == "out":
            result += str(R[t[1]])
            pos += 1
    return result


def find_pattern(r):
    n = 1
    while True:
        s = r[:n]
        found = True
        for i in range(1, len(r) // n):
            if r[i * n : i * n + n] != s:
                found = False
                break
        if found:
            break
        n += 1
    return r[:n]


a = 0
s = find_pattern(run([a, 0, 0, 0]))
while s != "01" * (len(s) // 2):
    a += 1
    s = find_pattern(run([a, 0, 0, 0]))
print("Part 1: ", a)
