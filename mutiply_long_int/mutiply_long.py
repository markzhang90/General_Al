__author__ = 'mark'

# mutiply big int
int_one = [1, 2, 3, 4, 5]
int_two = [5, 4, 3, 2, 6]


def multiply_long(first, second):
    first.reverse()
    second.reverse()
    z = [0] * (len(first) + len(second))
    for i in range(len(first)):
        for j in range(len(second)):

            z[i + j] += first[i] * second[j]

            if z[i + j] >= 10:
                z[i + j + 1] += z[i + j] / 10
                z[i + j] %= 10

    z.reverse()
    return z


print(multiply_long(int_one, int_two))
