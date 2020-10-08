def binary_search(arr, low, high, num):
    if high >= low:
        mid = (high + low) // 2
        if arr[mid] == num:
            return mid
        elif arr[mid] > num:
            return binary_search(arr, low, mid - 1, num)
        else:
            return binary_search(arr, mid + 1, high, num)
    else:
        return -1

