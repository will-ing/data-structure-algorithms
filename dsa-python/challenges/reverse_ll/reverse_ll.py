# from challenges.linked_list.linked_list import LinkedLists


class Node:

    def __init__(self, data=None, _next=None):

        self.data = data
        self._next = _next

    def __repr__(self):
        return f'{self.data} -> {self._next}'


class LinkedLists:
    def __init__(self, head=None):
        """
        this is intialized the Linked list

        Args:
            head ([any]): [Insert string or data etc]
        """
        self.head = head

    def __repr__(self):
        return f'{self.head}'

    def __str__(self):
        current = self.head
        return str(current)

    def insert(self, data):
        """
        This function inserts a new data in to the linked lists. Time complexity is O(1) which is fast

        Args:
            data ([any]): [Insert string or data etc]
        """
        new_node = Node(data)
        new_node._next(self.head)
        self.head = new_node

    def reverse_list(self):
        prev = None
        current = self.head
        while (current is not None):
            _next = current._next
            current._next = prev
            prev = current
            current = _next
        self.head = prev
