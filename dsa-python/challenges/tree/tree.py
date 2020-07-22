class TreeNode:
    """
    This is our node
    """

    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left_child = left
        self.right_child = right

    def __repr__(self):
        return f'{self.left_child}<- {self.val} -> {self.right_child}'


class BinarySearchTree():
    """
    This is for making binary search trees
    """

    def __init__(self, root=None):
        self.root = root

    def contains(self, val, root=None):
        if root is None or self.root.val == val:
            return self.root.val
        elif val < self.root.val:
            return self.contains(val, self.root.left_child)
        else:
            return self.contains(val, self.root.right_child)

    def add(self, val, root=None):
        if val < root.val:

            if root.left_child is None:
                root.left_child = TreeNode(val)
            else:
                self.add(val, self.root.left_child)

        elif val > self.root.val:

            if self.root.right_child is None:
                self.root.right_child = TreeNode(val)
            else:
                self.add(val, self.root.right_child)
