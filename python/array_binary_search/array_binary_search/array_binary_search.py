

def binarySearch(arr, x):
    """
    searches for the index of the arr and value that are passed through.
    If the value does not exist it will return -1

    arg(arr) = an array of any length

    arg(x) = x is the value you want to search
    """

    low = 0
    high = len(arr) - 1
    while(low <= high):
        mid = (low + high) // 2
        if arr[mid] == x:
            return mid
        elif x < arr[mid]:
            high = mid - 1
        elif x > arr[mid]:
            low = mid + 1
        else:
            break
    return -1

