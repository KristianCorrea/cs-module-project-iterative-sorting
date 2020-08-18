def linear_search(arr, target):
    ## iterate over the entire array
    for i in arr:
        if i == target:
            return arr.index(target)


    return -1   # not found


# Write an iterative implementation of Binary Search
def binary_search(arr, target):

    # Your code here
    low = 0
    high = len(arr)-1
    mid = 0

    while low <= high:
        mid = (low+high) // 2
        if arr[mid] < target:
            # go right
            low = mid + 1
        elif target < arr[mid]:
            # go left
            high = mid - 1
        else:
            # found
            return mid

    return -1  # not found
