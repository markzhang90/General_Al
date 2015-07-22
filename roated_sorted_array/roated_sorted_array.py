__author__ = 'mark'


# search element in a roated sorted array
def rotated_binary_sarch(arr, num):
    lenth_arr = len(arr)
    pivot = find_pivot(arr, 0, len(arr) - 1)
    if pivot == -1:
        binary_search(arr, 0, len(arr) - 1, num)
    else:
        if arr[pivot] == num:
            return pivot
        elif arr[0] <= num:
            return binary_search(arr, 0, pivot - 1, num)
        else:
            return binary_search(arr, pivot + 1, len(arr) - 1, num)


# standard binary search
def binary_search(arr, low, high, num):
    if low > high:
        return -1
    mid = (high + low) / 2
    if arr[mid] == num:
        return mid
    if num > arr[mid]:
        return binary_search(arr, mid + 1, high, num)
    else:
        return binary_search(arr, low, mid - 1, num)


# find pivot point
def find_pivot(arr, low, high):
    if low > high:
        return - 1
    mid = (low + high) / 2
    if mid > low and arr[mid] < arr[mid - 1]:
        return mid - 1
    if mid < high and arr[mid] > arr[mid + 1]:
        return mid
    if arr[low] >= arr[mid]:
        return find_pivot(arr, low, mid - 1)
    else:
        return find_pivot(arr, mid + 1, high)
arr = [4,5,6,7,1,2,3,4]
print find_pivot(arr, 0, len(arr)-1)