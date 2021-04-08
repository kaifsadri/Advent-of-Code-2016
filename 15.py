"""
Puzzle input:
Part 1:
Disc #1 has 17 positions; at time=0, it is at position 15.
Disc #2 has 3 positions; at time=0, it is at position 2.
Disc #3 has 19 positions; at time=0, it is at position 4.
Disc #4 has 13 positions; at time=0, it is at position 2.
Disc #5 has 7 positions; at time=0, it is at position 2.
Disc #6 has 5 positions; at time=0, it is at position 0.

part 2:
Disc #6 has 11 positions; at time=0, it is at position 0.
"""

# brute force is more than adequate. Chinese Remainder Theorem was probably intended.
# If the ball is dropped at time t, Disc n is at position [t+n+P0n]%Nn


def run(part):
    t = -1
    while True:
        t += 1
        if (t + 1 + 15) % 17 != 0:
            continue  # ball bounced
        if (t + 2 + 2) % 3 != 0:
            continue  # ball bounced
        if (t + 3 + 4) % 19 != 0:
            continue  # ball bounced
        if (t + 4 + 2) % 13 != 0:
            continue  # ball bounced
        if (t + 5 + 2) % 7 != 0:
            continue  # ball bounced
        if (t + 6 + 0) % 5 != 0:
            continue  # ball bounced
        if part == 2 and (t + 7 + 0) % 11 != 0:
            continue  # ball bounced
        break  # ball went through
    return t


print("Part 1: ", run(1))
print("Part 2: ", run(2))