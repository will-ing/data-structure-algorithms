from linked_list.linked_list import link_list


def test_empty_list():
    assert link_list.head == None


def test_insert():
    link_list.insert(3)
    assert link_list.__str__() == '3 -> None -> '


def test_head():
    link_list.insert(3)
    link_list.insert(2)
    link_list.insert(1)
    assert link_list.includes(1) == True


def test_insert_multiple():
    link_list.insert(4)
    link_list.insert(3)
    link_list.insert(2)
    link_list.insert(1)
    assert link_list.head == '1 -> 2 -> 3 -> 4 -> 1 -> 2 -> 3 -> 3 -> None'


def test_find_value():
    link_list.insert(3)
    link_list.insert(2)
    assert link_list.includes(3) == True


def test_no_find_value():
    link_list.insert(1)
    link_list.insert(2)
    assert link_list.includes(5) == False


def test_insert():
    assert link_list.__str__() == '3 -> None -> '
