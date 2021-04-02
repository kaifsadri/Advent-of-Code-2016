L = open("01.txt").readline().strip().split(', ')

direction = "N"
loc = [0,0]

T ={"L": {"N":"W", "W":"S", "S":"E","E":"N"},"R": {"S":"W", "E":"S", "N":"E","W":"N"}}
M = {"N":(0,1), "W":(-1,0), "S":(0,-1),"E":(1,0)}
S = set()

EBHQ=[0,0]

for ins in L:
    r = ins[0]
    l = int(ins[1:])
    direction = T[r][direction]
    for i in range(l):
        loc[0] += M[direction][0]
        loc[1] += M[direction][1]
        if tuple(loc) not in S:
            S.add(tuple(loc))
        elif EBHQ==[0,0]:
            EBHQ=tuple(loc)
   
# Part 1:
print("Part 1: ", abs(loc[0])+abs(loc[1]))
# Part 2:
print("Part 2: ", abs(EBHQ[0])+abs(EBHQ[1]))

