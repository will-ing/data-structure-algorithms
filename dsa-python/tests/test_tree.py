from challenges.tree.tree import TreeNode, BinarySearchTree, BinaryTree


def test_tree():
    node = TreeNode(3, 1, 5)
    new_tree = BinarySearchTree(node)
    assert new_tree.root.val == 3
    assert new_tree.root.left_child == 1
    assert new_tree.root.right_child == 5


def test_contains():
    node = TreeNode(3, 1, 5)
    new_tree = BinarySearchTree(node)
    assert new_tree.contains(3) == True


def test_add():
    node = TreeNode(3)
    new_tree = BinarySearchTree(node)
    new_tree.add(9)
    new_tree.add(2)
    new_tree.add(1)
    assert new_tree.contains(1) == True


def test_in_order():
    node9 = TreeNode(9)
    node1 = TreeNode(1)
    node = TreeNode(5, node1, node9)
    new_tree = BinaryTree(node)
    actual = new_tree.in_order()
    expected = [1, 5, 9]
    assert actual == expected


def test_pre_order():
    node9 = TreeNode(9)
    node1 = TreeNode(1)
    node = TreeNode(5, node1, node9)
    new_tree = BinaryTree(node)
    actual = new_tree.pre_order()
    expected = [5, 1, 9]
    assert actual == expected


def test_post_order():
    node9 = TreeNode(9)
    node1 = TreeNode(1)
    node = TreeNode(5, node1, node9)
    new_tree = BinaryTree(node)
    actual = new_tree.post_order()
    expected = [1, 9, 5]
    assert actual == expected


def test_max():
    node6 = TreeNode(6)
    node3 = TreeNode(3)
    node2 = TreeNode(2)
    node9 = TreeNode(9, TreeNode(7, node6))
    node1 = TreeNode(1, TreeNode(4, node3, node2))
    node = TreeNode(5, node1, node9)
    print(node)
    new_tree = BinaryTree(node)
    actual = new_tree.find_max()
    expected = 9
    assert actual == expected


def est_breadth():
    node6 = TreeNode(6)
    node3 = TreeNode(3)
    node2 = TreeNode(2)
    node9 = TreeNode(9, TreeNode(7, node6))
    node1 = TreeNode(1, TreeNode(4, node3, node2))
    node = TreeNode(5, node1, node9)
    new_tree = BinaryTree(node)
    actual = new_tree.breadth()
    expected = [5, 1, 9, 7, 4, 6, 2]
    assert actual == expected
