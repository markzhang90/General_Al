__author__ = 'mark'
import copy


# Given a collection of distinct numbers, return all possible permutations.
#
# For example,
# [1,2,3] have the following permutations:
# [
#   [1,2,3],
#   [1,3,2],
#   [2,1,3],
#   [2,3,1],
#   [3,1,2],
#   [3,2,1]
# ]


def call_back(all_list, res):
    if not any(all_list):
        print(res)
        return 0

    this_value = all_list.pop(0)
    if not any(res):
        value = [this_value]
        res.append(value)
        call_back(all_list, res)
    else:
        new_res = []
        for one_line in res:
            for i in range(len(one_line) + 1):
                new_one_line = copy.copy(one_line)
                new_one_line.insert(i, this_value)
                new_res.append(new_one_line)
        del res
        call_back(all_list, new_res)


temp = []
my_list = [1, 2, 3, 5, 6]
call_back(my_list, temp)
