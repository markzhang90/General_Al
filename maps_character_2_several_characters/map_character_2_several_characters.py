__author__ = 'mark'
str = "face"
mapping = {
    'f': ['f', '@', '4', 'h'],
    'a': ['a', 'c', 'e']
}


def change_str(str, map, index):
    if index >= len(str):
        print ''.join(str)
        return

    else:
        print str[index]
        if str[index] in map:
            for one_replace in map.get(str[index]):
                temp = list(str)
                temp[index] = one_replace
                ''.join(temp)
                change_str(temp, map, index + 1)
        else:
            change_str(str, map, index + 1)


change_str(str, mapping, 0)
