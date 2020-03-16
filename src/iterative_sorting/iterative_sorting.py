# TO-DO: Complete the selection_sort() function below
def selection_sort(arr):
    # loop through n-1 elements
    # note that the 2nd value in the range specification is non inclusive. So this goes to len(arr)-1
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc)
        for j in range(cur_index + 1, len(arr)):
            if arr[j] < arr[smallest_index]:
                smallest_index = j

        # TO-DO: swap
        temp = arr[smallest_index]
        arr[smallest_index] = arr[cur_index]
        arr[cur_index] = temp

    return arr





# TO-DO:  implement the Bubble Sort function below
def bubble_sort(arr):

    # swap_done indicates if a swap was done in the nested if statement within the while
    # loop below. Must start out True to enter the while loop
    swap_done = True

    while swap_done:
        # Inside the while loop, only a swap action can set swap_done to True
        swap_done = False
        for i in range(0, len(arr) - 1):
            if arr[i] > arr[i + 1]:
                temp = arr[i + 1]
                arr[i + 1] = arr[i]
                arr[i] = temp
                swap_done = True

    return arr





# STRETCH: implement the Count Sort function below
def count_sort(arr, maximum=-1):

    return arr
