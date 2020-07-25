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


class BinaryTree:
    """
    Class that creates binary trees
    """

    def __init__(self, root=None):
        self.root = root

    # def preOrder(self):


class BinarySearchTree:
    """
    This is for making binary search trees

    REF: https://gist.github.com/jakemmarsh/8273963
    """

    def __init__(self, root=None):
        self.root = root

    def __repr__(self):
        return f'{self.root}'

    def __str__(self):
        current = self.root
        return str(current)

    def contains(self, val, root=None):
        if root is None or self.root.val == val:
            return True
        elif val < self.root.val:
            return self.contains(val, self.root.left_child)
        elif val > self.root.val:
            return self.contains(val, self.root.right_child)
        else:
            return False

    def add(self, val):

        if (self.root is None):
            self.root = TreeNode(val)
        else:
            self.add_node(val, self.root)

    def add_node(self, val, c_node):

        if val < c_node.val:
            if c_node.left_child:
                self.add_node(val, c_node.left_child)
            else:
                c_node.left_child = TreeNode(val)

        if val > c_node.val:
            if c_node.right_child:
                self.add_node(val, c_node.right_child)
            else:
                c_node.right_child = TreeNode(val)
