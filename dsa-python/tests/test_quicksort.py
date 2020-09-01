from challenges.quicksort.quicksort import partition, quickSort


def test_quicksort():
    arr = [8, 4, 23, 42, 16, 15]
    list_len = len(arr)
    quickSort(arr, 0, list_len - 1)
    assert arr == [4, 8, 15, 16, 23, 42]


def test_reverse():
    arr = [20, 18, 12, 8, 5, -2]
    list_len = len(arr)
    quickSort(arr, 0, list_len - 1)
    assert arr == [-2, 5, 8, 12, 18, 20]


def test_unique():
    arr = [5, 12, 7, 5, 5, 7]
    list_len = len(arr)
    quickSort(arr, 0, list_len - 1)
    assert arr == [5, 5, 5, 7, 7, 12]


def test_nearly():
    arr = [2, 3, 5, 7, 13, 11]
    list_len = len(arr)
    quickSort(arr, 0, list_len - 1)
    assert arr == [2, 3, 5, 7, 11, 13]
