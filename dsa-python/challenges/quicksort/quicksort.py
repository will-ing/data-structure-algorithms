def partition(arr, left, right):
    i = (left - 1)
    pvt = arr[right]
    for j in range(left, right):
        if arr[j] <= pvt:
            i = i + 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i+1], arr[right] = arr[right], arr[i+1]
    return (i + 1)


def quickSort(arr, left, right):
    if left < right:
        index = partition(arr, left, right)
        quickSort(arr, left, index - 1)
        quickSort(arr, index + 1, right)
