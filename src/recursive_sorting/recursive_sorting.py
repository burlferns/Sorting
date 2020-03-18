# TO-DO: complete the helpe function below to merge 2 sorted arrays
def merge(arrA, arrB):
    elements = len(arrA) + len(arrB)
    merged_arr = [0] * elements
    # TO-DO
    indexA = 0  # current index for arrA
    indexB = 0  # current index for arrB
    indexM = 0  # current index for merged_arr
    lenA = len(arrA)
    lenB = len(arrB)

    # Take from the arrA or arrB as long as they are both not empty
    # Take from whichever is smaller at the indexA/B of the arrays
    while indexA < lenA and indexB < lenB:
        if arrA[indexA] < arrB[indexB]:
            merged_arr[indexM] = arrA[indexA]
            indexA += 1
            indexM += 1
        else:
            merged_arr[indexM] = arrB[indexB]
            indexB += 1
            indexM += 1

    # If arrB is all used up, then take from arrA only
    while indexA < lenA:
        merged_arr[indexM] = arrA[indexA]
        indexA += 1
        indexM += 1

    # If arrA is all used up, then take from arrB only
    while indexB < lenB:
        merged_arr[indexM] = arrB[indexB]
        indexB += 1
        indexM += 1

    return merged_arr


# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort(arr):
    # TO-DO
    if len(arr) > 1:
        half_point = int(len(arr) / 2)
        arrA = merge_sort(arr[0:half_point])
        arrB = merge_sort(arr[half_point:])
        arr = merge(arrA, arrB)

    return arr





# STRETCH: implement an in-place merge sort algorithm
def merge_in_place(arr, start, mid, end):
    # TO-DO

    return arr

def merge_sort_in_place(arr, l, r):
    # TO-DO

    return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort(arr):

    return arr
