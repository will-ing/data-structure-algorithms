
def insertion_sort(arr: list) -> list:
    """
    This sorts an array of integers in ascending order

    Args:
        arr (list): A unsorted list of ints

    Returns:
        list: a sorted list of ints
    """

    for i in range(1, len(arr)):
        temp = arr[i]
        j = i-1
        while j >= 0 and temp < arr[j]:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = temp
    return arr
