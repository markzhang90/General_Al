__author__ = 'mark'


# combination

def combination(elements, k, temp, res, x):
    if k == len(temp):
        res.append([m for m in temp])
        # print res
        return
    if x == len(elements):
        return

    else:
        for i in range(x, len(elements)):
            temp.append(elements[i])
            combination(elements, k, temp, res, i + 1)
            del temp[-1]


res = []
temp = []
list = [1, 2, 4, 3, 9]
combination(list, 2, temp, res, 0)
print res
