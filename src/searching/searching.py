# STRETCH: implement Linear Search
def linear_search(arr, target):
    # TO-DO: add missing code
    for i, n in enumerate(arr):
        if n == target:
            return i

    return -1   # not found


# STRETCH: write an iterative implementation of Binary Search
def binary_search(arr, target):

    if len(arr) == 0:
        return -1  # array empty

    low = 0
    high = len(arr) - 1

    # TO-DO: add missing code
    while True:
        half_point = int((high - low) / 2) + low
        if arr[half_point] == target:
            return half_point
        elif target < arr[half_point]:
            high = half_point - 1
        else:
            low = half_point + 1
        if high < low:
            return -1




# STRETCH: write a recursive implementation of Binary Search
def binary_search_recursive(arr, target, low, high):

    middle = (low + high) // 2

    if len(arr) == 0:
        return -1  # array empty
    # TO-DO: add missing if/else statements, recursive calls
    if arr[middle] == target:
        return middle
    elif target < arr[middle]:
        high = middle - 1
    else:
        low = low + 1
    if high < low:
        return -1
    return binary_search_recursive(arr, target, low, high)
