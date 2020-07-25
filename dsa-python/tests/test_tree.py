from challenges.tree.tree import TreeNode, BinarySearchTree


def test_tree():
    node = TreeNode(1, 3, 5)
    new_tree = BinarySearchTree(node)
    assert new_tree.root.val == 1
    assert new_tree.root.left_child == 3
    assert new_tree.root.right_child == 5


def test_contains():
    node = TreeNode(1, 3, 5)
    new_tree = BinarySearchTree(node)
    assert new_tree.contains(3) == True


def test_add():
    node = TreeNode(3)
    new_tree = BinarySearchTree(node)
    new_tree.add(9)
    new_tree.add(2)
    new_tree.add(1)
    assert new_tree.contains(1) == True
