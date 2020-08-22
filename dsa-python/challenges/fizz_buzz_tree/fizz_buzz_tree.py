from challenges.stack_and_queues.stack_and_queues import Queue


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

    def fizz_buzz(self, value):
        """
        Finds out if value is divisble by 3 or 5 or both

        Args:
            value int: A node value

        Returns:
            str: A string pending what the value is divisible by
        """
        if (value % 3 == 0) and (value % 5 == 0):
            return 'FizzBuzz'
        elif (value % 5) == 0:
            return 'Buzz'
        elif (value % 3) == 0:
            return 'Fizz'
        else:
            return str(value)

    def fizz_buzz_tree(self):
        """
        Creates a new tree with nodes that have string values of fizz or buzz

        Returns:
            tree: returns a new binary tree.
        """
        que = Queue()

        new_tree = self

        que.enqueue(new_tree.root)

        while que.is_empty() != True:
            node = que.dequeue()

            node.val = self.fizz_buzz(node.val)

            if node.right_child:
                que.enqueue(node.right_child)

            if node.left_child:
                que.enqueue(node.left_child)

        return new_tree
