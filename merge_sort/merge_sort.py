__author__ = 'mark'

# merge sort

arr = [2, 3, 4, 5, 1, 2, 4, 5, 6, -2, 12, 2, 4, 5, 21, 4]


def merge_sort(arr, low, high):
    if high > low:
        mid = (low + high) / 2
        merge_sort(arr, low, mid)
        merge_sort(arr, mid + 1, high)
        merge_array(arr, low, mid, high)
    return arr


def merge_array(arr, low, mid, high):
    i = low
    j = mid + 1
    temp = []
    while i <= mid and j <= high:
        if arr[i] <= arr[j]:
            temp.append(arr[i])
            i += 1
        else:
            temp.append(arr[j])
            j += 1
    while i <= mid:
        temp.append(arr[i])
        i += 1
    while j <= high:
        temp.append(arr[j])
        j += 1

    for k in range(len(temp)):
        arr[low + k] = temp[k]


print merge_sort(arr, 0, len(arr) - 1)
