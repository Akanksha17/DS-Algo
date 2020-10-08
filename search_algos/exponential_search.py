from .binary_search import binary_search


# O(logn)
# Find range where element is present
# Do Binary Search in above found range.


def exponential_search(arr, num):
    if arr[0] == num:
        return 0
    i = 1
    arr_len = len(arr)
    while i < arr_len and arr[i] <= num:
        i = i**2
        return binary_search(arr, i//2, min(i, arr_len), num)
