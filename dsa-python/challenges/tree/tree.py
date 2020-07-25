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

    def in_order(self):
        """
        Driver Function that orders from left to root to right nodes

        Returns:
            [List]: [left, root, right]
        """
        return self.in_order_go(self.root)

    def in_order_go(self, root=None):
        """
        recursive function to get values
        """
        return (self.in_order_go(root.left_child) + [root.val] + self.in_order_go(root.right_child)) if root else []

    def pre_order(self):
        """
        Driver Function that orders from root to left to right nodes

        Returns:
            [List]: [root, left, right]
        """
        return self.pre_order_go(self.root)

    def pre_order_go(self, root=None):
        return ([root.val] + self.pre_order_go(root.left_child) + self.pre_order_go(root.right_child)) if root else []

    def post_order(self):
        """
         Driver Function that orders from left to right root to nodes

         Returns:
             [List]: [root, left, right]
         """
        return self.post_order_go(self.root)

    def post_order_go(self, root):
        return (self.post_order_go(root.left_child) + self.post_order_go(root.right_child) + [root.val]) if root else []


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

    def contains(self, val):
        return self.contains_node(val, self.root)

    def contains_node(self, val, root=None):
        if root.val is val:
            return True
        if root.val is None:
            return False
        elif val < root.val:
            return self.contains_node(val, root.left_child)
        elif val > root.val:
            return self.contains_node(val, root.right_child)
        else:
            raise TypeError('Must be an Integer')

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
