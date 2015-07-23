__author__ = 'mark'

# quick sort

arr = [2, 3, 4, 5, 1, 2, 4, 5, 6, -2, 12, 2, 4, 5, 21, 4]


def quick_sort(arr, first, last):
    if last > first:

        i = first
        temp = arr[i]
        j = last
        while i < j:
            while arr[j] >= temp and i < j:
                j -= 1
            if i < j:
                arr[i] = arr[j]
                i += 1
            while arr[i] <= temp and i < j:
                i += 1
            if i < j:
                arr[j] = arr[i]
                j -= 1
        arr[i] = temp
        quick_sort(arr, first, i - 1)
        quick_sort(arr, i + 1, last)
    return arr


print quick_sort(arr, 0, len(arr) - 1)
