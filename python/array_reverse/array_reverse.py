arr = [1, 2, 3, 4, 5]


def reverse_array(lst):  # returns the same list but in reverse
    lst.reverse()
    print(lst)


def reverse_array_copy(lst):  # creates new list that is reversed
    copy_lst = lst[::-1]
    print(copy_lst)


reverse_array_copy(arr)


def reversed_array(lst):  # reversed doesn't modify the original
    print(list(reversed(lst)))


reversed_array(arr)

reverse_array(arr)
