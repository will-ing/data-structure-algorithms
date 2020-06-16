from linked_list.linked_list import link_list, LinkedLists, Node


# def test_empty_list():
#     assert link_list.head == None


# def test_insert():
#     link_list.insert(3)
#     assert link_list.__str__() == '3 -> None -> '


# def test_head():
#     link_list.insert(3)
#     link_list.insert(2)
#     link_list.insert(1)
#     assert link_list.includes(1) == True


# def test_insert_multiple():
#     link_list.insert(4)
#     link_list.insert(3)
#     link_list.insert(2)
#     link_list.insert(1)
#     assert link_list.head == '1 -> 2 -> 3 -> 4 -> 1 -> 2 -> 3 -> 3 -> None'


# def test_find_value():
#     link_list.insert(3)
#     link_list.insert(2)
#     assert link_list.includes(3) == True


# def test_no_find_value():
#     link_list.insert(1)
#     link_list.insert(2)
#     assert link_list.includes(5) == False


# def test_insert():
#     assert link_list.__str__() == '3 -> None -> '


def test_append():
    linky = LinkedLists()
    linky.append_to_end(5)
    linky.append_to_end(6)
    assert linky.head.next_node.data == 6


def test_append_multi():
    link2 = LinkedLists()
    link2.append_to_end(5)
    link2.append_to_end(6)
    link2.append_to_end(7)
    link2.append_to_end(8)
    assert link2.__str__() == '5 -> 6 -> 7 -> 8 -> None'


def test_insert_after_node():
    link3 = LinkedLists()
    link3.append_to_end('five')
    link3.append_to_end(6)
    link3.append_to_end(7)
    link3.append_to_end(8)
    link3.insert_after(8, 9)
    actual = link3.__str__()
    expected = 'five -> 6 -> 7 -> 8 -> 9 -> None'
    assert actual == expected


def test_insert_after_node_mid():
    link4 = LinkedLists()
    link4.append_to_end('five')
    link4.append_to_end(6)
    link4.append_to_end(7)
    link4.append_to_end(8)
    link4.append_to_end(10)
    link4.insert_after(7, 9)
    actual = link4.__str__()
    expected = 'five -> 6 -> 7 -> 9 -> 8 -> 10 -> None'
    assert actual == expected


def test_insert_before_node():
    link5 = LinkedLists()
    link5.append_to_end('five')
    link5.append_to_end(6)
    link5.append_to_end(7)
    link5.append_to_end(8)
    link5.append_to_end(10)
    link5.insert_before(7, 9)
    actual = link5.__str__()
    expected = 'five -> 6 -> 9 -> 7 -> 8 -> 10 -> None'
    assert actual == expected


def test_insert_before_node():
    link6 = LinkedLists()
    link6.append_to_end('five')
    link6.append_to_end(6)
    link6.append_to_end(7)
    link6.append_to_end(8)
    link6.append_to_end(10)
    link6.insert_before('five', 9)
    actual = link6.__str__()
    expected = '9 -> five -> 6 -> 7 -> 8 -> 10 -> None'
    assert actual == expected
