__author__ = 'mark'
str1 = "Geeksdas"
str2 = ":Geeksdas"


class Longest:
    max_value = 0

    def longest_sub_string(self, str1, str2, i, j, temp):
        str1_len = len(str1)
        str2_len = len(str2)
        if i >= str1_len:
            return 0
        if j >= str2_len:
            return 0
        if str1[i] == str2[j]:
            temp += 1
            if self.max_value < temp:
                self.max_value = temp
            self.longest_sub_string(str1, str2, i + 1, j + 1, temp)

        else:
            self.longest_sub_string(str1, str2, i + 1, j, 0)
            self.longest_sub_string(str1, str2, i, j + 1, 0)


test = Longest()
test.longest_sub_string(str1, str2, 0, 0, 0)
print test.max_value


def lcs(xstr, ystr):
    if not xstr or not ystr:
        return ''
    x, xs, y, ys = xstr[0], xstr[1:], ystr[0], ystr[1:]
    if x == y:
        return x + lcs(xs, ys)
    else:
        return max(lcs(xstr, ys), lcs(xs, ystr), key=len)


def lcs(a, b):
    lengths = [[0 for j in range(len(b) + 1)] for i in range(len(a) + 1)]
    # row 0 and column 0 are initialized to 0 already
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            if x == y:
                lengths[i + 1][j + 1] = lengths[i][j] + 1
            else:
                lengths[i + 1][j + 1] = max(lengths[i + 1][j], lengths[i][j + 1])
    # read the substring out from the matrix
    result = ""
    x, y = len(a), len(b)
    while x != 0 and y != 0:
        if lengths[x][y] == lengths[x - 1][y]:
            x -= 1
        elif lengths[x][y] == lengths[x][y - 1]:
            y -= 1
        else:
            assert a[x - 1] == b[y - 1]
            result = a[x - 1] + result
            x -= 1
            y -= 1
    return result


print lcs('geeksdas', 'lgeekslldas')
