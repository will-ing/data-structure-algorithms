

def merge(arr: list, left, middle, right):
    """
    sorts through array and merges them back together.

    Args:
        arr (list): [array that needs to be sorted]
        left (int): [left of array]
        middle (int): [the mid of the array]
        right (int): [right of array]
    """
    a1 = middle - left + 1
    a2 = right - middle

    left_arr = [0] * (a1)
    right_arr = [0] * (a2)

    i = 0
    j = 0
    k = left

    for i in range(0, a1):
        left_arr[i] = arr[left + i]

    for j in range(0, a2):
        right_arr[j] = arr[middle + 1 + j]

    while i < a1 and j < a2:
        if left_arr[i] <= right_arr[j]:
            arr[k] = left_arr[i]
            i += 1
        else:
            arr[k] = right_arr[j]
            j += 1
        k += 1

    while i < a1:
        arr[k] = left_arr[i]
        i += 1
        k += 1

    while j < a2:
        arr[k] = right_arr[j]
        j += 1
        k += 1


def mergeSort(arr):
    """
    Driver method for the the merge. Uses divide and conquer to sort arrays

    Args:
        arr (list): [whole array]
        left (list): [left side of of array]
        right (list): [right side of array]
    """
    n = len(arr)

    if n > 1:
        mid = n // 2
        left = arr[mid:]
        right = arr[:mid]
        l = 0
        r = n

        mergeSort(left)
        mergeSort(right)
        merge(arr, l, mid, r)
