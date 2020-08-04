from challenges.fizz_buzz_tree.fizz_buzz_tree import BinaryTree, TreeNode, Queue


def test_proof_of_life():
    assert True == True


def test_fizz():
    node5 = TreeNode(5)
    node3 = TreeNode(3)
    node15 = TreeNode(15)
    node5.left_child = node15
    node5.right_child = node3
    b_tree = BinaryTree(node5)
    b_tree.fizz_buzz_tree()
    expected = b_tree.root.left_child
    actual = 'Fizz'
    assert expected == actual


def test_buzz():
    node5 = TreeNode(5)
    node3 = TreeNode(3)
    node15 = TreeNode(15)
    node5.left_child = node15
    node5.right_child = node3
    b_tree = BinaryTree(node5)
    b_tree.fizz_buzz_tree()
    expected = b_tree.root.val
    actual = 'Buzz'
    assert expected == actual


def test_fizz_buzz():
    pass


def test_string():
    pass
