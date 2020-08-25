

def merge(arr: list, left: list, middle: list, right: list):
    """
    sorts through array and merges them back together.

    Args:
        arr (list): [array that needs to be sorted]
        left (list): [left of mid of array]
        middle (list): [the mid of the array]
        right (list): [right of mid of array]
    """
    a1 = middle - left + 1
    a2 = right - middle

    left_arr = [0] * (a1)
    right_arr = [0] * (a2)

    for i in range(0, a1):
        left_arr[i] = arr[left + i]

    for j in range(0, a2):
        right_arr[j] = arr[middle + 1 + j]

    i = 0
    j = 0
    k = left

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


def mergeSort(arr, left=0, right=None):
    """
    Driver method for the the merge. Uses divide and conquer to sort arrays

    Args:
        arr (list): [whole array]
        left (list): [left side of of array]
        right (list): [right side of array]
    """

    right = len(arr) - 1

    if left < right:

        mid = (left+(right-1))//2

        mergeSort(arr, left, mid)
        mergeSort(arr, mid+1, right)
        merge(arr, left, mid, right)
