class Node:
    """
    This is our node
    """

    def __init__(self, value, next_=None):
        """
        This initializes the node 

        Args:
            value ([any]): [This can be a string, integer, etc]
            next_ ([object], optional): [this is the value of the next node]. Defaults to None.
        """
        self.value = value
        self.next_ = next_


class LinkedLists:
    """
    This class creates linked lists
    """

    def __init__(self):
        """
        this is intialized the Linked list
        """

        self.head = None

    def insert(self, value):
        """
        This function inserts a new value in to the linked lists

        Args:
            value ([any]): [Insert string or value etc]
        """

        node = Node(value)

        if self.head is not None:
            node.next_ = self.head
        self.head = node

    def includes(self, value):
        """
        this function checks to see if a value is in the linked lists and return boolean

        Args:
            value ([any]): [as long as the value type is in the list it will return true]
        """
