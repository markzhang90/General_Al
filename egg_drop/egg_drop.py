__author__ = 'mark'
import sys


table = [[None]*101 for i in range(101)]


def egg_drop(floor, egg_num):
    global table

    if floor == 1:
        return 1

    if floor == 0:
        return 0

    if egg_num == 1:
        return floor

    if egg_num == 0:
        return 0

    min_val = sys.maxsize

    for x in range(1, floor):
        result = 1 + max(memrize(x-1, egg_num-1), memrize(floor-x, egg_num))

        if result < min_val:
            min_val = result

    return min_val


def memrize(floor, egg_num):
    global table
    if table[floor][egg_num] is not None:
        return table[floor][egg_num]

    table[floor][egg_num] = egg_drop(floor, egg_num)
    return table[floor][egg_num]

val = egg_drop(100, 2)

print(val)
for x in table:
    print(x)
