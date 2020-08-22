from challenges.insertion_sort.insertion_sort import insertion_sort as ins


def test_sort():
    ay = [8, 4, 23, 42, 16, 15]
    assert ins(ay) == [4, 8, 15, 16, 23, 42]


def test_reversed():
    ay = [20, 18, 12, 8, 5, -2]
    assert ins(ay) == [-2, 5, 8, 12, 18, 20]


def test_uniques():
    ay = [5, 12, 7, 5, 5, 7]
    assert ins(ay) == [5, 5, 5, 7, 7, 12]


def test_nearly():
    ay = [2, 3, 5, 7, 13, 11]
    assert ins(ay) == [2, 3, 5, 7, 11, 13]
