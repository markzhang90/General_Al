# heap sort

arr = [2, 3, 4, 5, 1, 2, 4, 5, 6, -2, 12, 2, 4, 5, 21, 4]


def heapfy(arr):
    parent = (len(arr) - 1) / 2
    while parent >= 0:
        heapit(arr, parent, len(arr) - 1)
        parent -= 1
    cursor = len(arr) - 1
    while cursor >= 0:
        swap(arr, 0, cursor)
        cursor -= 1
        heapit(arr, 0, cursor)


def heapit(arr, current, last):
    l = 2 * current + 1
    r = 2 * (current + 1)
    max = current
    if l <= last and arr[current] < arr[l]:
        max = l

    if r <= last and arr[max] < arr[r]:
        max = r
    if max != current:
        swap(arr, max, current)
        heapit(arr, max, last)


def swap(arr, a, b):
    arr[a], arr[b] = arr[b], arr[a]


heapfy(arr)
print arr
