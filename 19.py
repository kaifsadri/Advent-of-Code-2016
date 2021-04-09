from collections import deque

L = 3017957  # puzzle input
E = deque(range(1, L + 1))
while len(E) > 1:
    E.append(E.popleft())
    E.popleft()
print("Part 1: ", E[0])

R = deque(range(1, L // 2 + 1))
L = deque(range(L, L // 2, -1))
while L and R:
    if len(R) > len(L):
        R.pop()
    else:
        L.pop()
    try:  # this rotates the picture. except clause takes care of even L
        R.append(L.pop())
        L.appendleft(R.popleft())
    except IndexError:
        break
if R:
    print("Part 2: ", R[0])
else:
    print("Part 2: ", L[0])
