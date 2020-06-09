from array_binary_search.array_binary_search import binarySearch

"""
Write a function called BinarySearch which takes in 2 
parameters: a sorted array and the search key. 
Without utilizing any of the built-in methods available to your 
language, return the index of the array’s element that is equal 
to the search key, or -1 if the element does not exist.
"""


def test_binary_search_one():
    arr = [1, 15, 30, 45, 46, 49]
    actual = binarySearch(arr, 15)
    expected = 1
    assert actual == expected


def test_binary_search_two():
    arr = [4, 100, 1000, 1050, 1052, 1053, 1500, 1576]
    actual = binarySearch(arr, 1576)
    expected = 7
    assert actual == expected


def test_binary_search_three():
    arr = [1, 2, 3, 4, 5, 6, 9, 11, 12, 13, 14, 15, 16]
    actual = binarySearch(arr, 15)
    expected = 11
    assert actual == expected


def test_binary_search_four():
    arr = [1, 2, 3, 4, 5, 6, 9, 11, 12, 13, 14, 15, 16]
    actual = binarySearch(arr, 7)
    expected = -1
    assert actual == expected
