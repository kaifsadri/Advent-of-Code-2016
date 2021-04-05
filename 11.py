# The absolute minimum number of moves required to take
# n objects from floor x to floor x+1 is N = (n-2)*2 + 1 = 2*n - 3.
# n-2 objects are moved each with 2 moves (take 2 up, one down), then 1 move for last two.
# For each puzzle arrangement, the total sum is calculated by adding:
# N(take all objects on floor 1 to floor 2) +
# N(take all obhe4, 2, 4, 0]cts on 2 to 3) + ... until all are on floor 4.


def N(F):
    return sum([sum(F[0 : i + 1]) * 2 - 3 for i in range(len(F))])


# Part 1:
# Puzzle input:
A = [4, 2, 4]
print("Part 1: ", N(A))

# Part 2:
# Puzzle input:
A = [8, 2, 4]
print("Part 2: ", N(A))
