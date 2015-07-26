__author__ = 'mark'

arr = [1, 2, 3, 2, 5, 6, 7, 8, 3, 2, 4, 5, 2, 21, 2, 3, 4, 5, 6, 7, 8, 9, 10]


def longest_asc(arr):
    max_leng = 0
    leng = 0
    pre_max = 0
    for i in arr:
        if i > pre_max:
            leng += 1
            pre_max = i
        else:
            leng = 1
            pre_max = i
        if leng > max_leng:
            max_leng = leng
    return max_leng


print longest_asc(arr)
