

class Node:
    """
    This is our node
    """

    def __init__(self, data=None, next_node=None):
        """
        This initializes the node

        Args:
            data ([any]): [This can be a string, integer, etc]
            next_node ([object], optional): [this is the data of the next node]. Defaults to None.
        """
        self.data = data
        self.next_node = next_node

    def __repr__(self):
        return f'{self.data} -> {self.next_node}'


class Stack:
    """
    This a class to build stacks
    """

    def __init__(self):
        self.top = None

    def push(self, data):
        """
        Push data on op of the stack.

        Args:
            data (data): [add data you want in the stack]
        """
        self.top = Node(data, self.top)

    def pop(self):
        """
        removes the top of the stack

        Returns:
            top of stack: [description]
        """
        if self.top is None:
            raise AttributeError("Stack is empty")
        else:
            ptr = self.top
            self.top = self.top.next_node
            ptr.next = None
            return ptr.data

    def is_empty(self):
        if self.top is None:
            return True
        else:
            return False

    def peek(self):
        if self.top is None:
            raise AttributeError('Stack is empty')
        else:
            return self.top.data


class Queue:
    """
    creates a Queue
    """

    def __init__(self):
        self.front = None

    def enqueue(self, data):
        self.front = Node(data, self.front)

    def dequeue(self):
        if self.front:
            ptr = self.front
            self.front = self.front.next_node
            ptr.next = None
            return ptr.data
        else:
            raise AttributeError('The queue is empty')

    def peek(self):
        if self.front is None:
            raise AttributeError('The queue is empty')
        else:
            return self.front.data

    def is_empty(self):
        if self.front is None:
            return True
        else:
            return False
