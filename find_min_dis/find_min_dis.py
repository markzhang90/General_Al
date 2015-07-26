__author__ = 'mark'
"""
Algorithm to find the two numbers whose difference is minimum among the set of numbers.
For example the sequence is 5, 13, 7, 0, 10, 20, 1, 15, 4, 19
The algorithm should return min diff = 20-19 = 1.
Constraint - Time Complexity O(N) & Space is not a constraint [upto O(3N)]
Assumption - Sorting O(nlogn) & comparison of adjacent numbers is already known & is
not an option. Try to keep it linear
"""

arr = [5, 13, 7, 0, 10, 20, 1, 15, 4, 19]


def find_min(arr, i, min):
    if i >= len(arr):
        return min
    temp = arr[i]
    j = i
    while j > 0:
        if arr[j] <= arr[j - 1]:
            arr[j - 1], arr[j] = arr[j], arr[j - 1]
            j -= 1
        else:
            break
    print arr
    if j > 0:
        if arr[j] - arr[j - 1] <= min:
            min = arr[j] - arr[j - 1]
    if j < len(arr) - 1 and j != i:
        if arr[j + 1] - arr[j] <= min:
            min = arr[j + 1] - arr[j]
    return find_min(arr, i + 1, min)


min_value = 100
print find_min(arr, 1, min_value)
