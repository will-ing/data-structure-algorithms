class TreeNode:
    """
    This is our node
    """

    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left_child = left
        self.right_child = right

    def __repr__(self):
        return f'Root: {self.val} \nLeft: {self.left_child} \nRight: {self.right_child}'


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
        return self.in_order_recur(self.root)

    def in_order_recur(self, root=None):
        """
        recursive function to get values
        """
        return (self.in_order_recur(root.left_child) + [root.val] + self.in_order_recur(root.right_child)) if root else []

    def pre_order(self):
        """
        Driver Function that orders from root to left to right nodes

        Returns:
            [List]: [root, left, right]
        """
        return self.pre_order_recur(self.root)

    def pre_order_recur(self, root=None):
        return ([root.val] + self.pre_order_recur(root.left_child) + self.pre_order_recur(root.right_child)) if root else []

    def post_order(self):
        """
         Driver Function that orders from left to right root to nodes

         Returns:
             [List]: [root, left, right]
         """
        return self.post_order_recur(self.root)

    def post_order_recur(self, root):
        return (self.post_order_recur(root.left_child) + self.post_order_recur(root.right_child) + [root.val]) if root else []

    def find_max(self):
        """
        Returns the max value in a binary tree.

        Returns:
            [int]: Max integer in tree
        """
        return self.find_max_recurse(self.root)

    def find_max_recurse(self, current=None):
        if current is None:
            return 0

        tree_max = current.val
        left_max = self.find_max_recurse(current.left_child)
        right_max = self.find_max_recurse(current.right_child)

        if (left_max > tree_max):
            tree_max = left_max
        if (right_max > tree_max):
            tree_max = right_max
        return tree_max


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
