def partition(arr, left, right):
    """
    Goes through an array and sorts in using pointer and pivots

    Args:
        arr ([list]): [List you want to sort]
        left ([int]): [left pointer]
        right ([int]): [right pointer]

    Returns:
        [int]: [index of the partition]
    """
    i = (left - 1)
    pvt = arr[right]
    for j in range(left, right):
        if arr[j] <= pvt:
            i = i + 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i+1], arr[right] = arr[right], arr[i+1]
    return (i + 1)


def quickSort(arr: list, left: int, right: int):
    """
    quickly sorts through an array

    Args:
        arr (list): List you want to sort
        left (int): left pointer
        right (int): right pointer
    """
    if left < right:
        index = partition(arr, left, right)
        quickSort(arr, left, index - 1)
        quickSort(arr, index + 1, right)
