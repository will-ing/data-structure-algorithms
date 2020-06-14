# ref (https://www.codefellows.org/blog/implementing-a-singly-linked-list-in-python/)
# author: John Shiver

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

    def get_data(self):
        return self.data

    def get_next(self):
        return self.next_node

    def set_next(self, new_next):
        self.next_node = new_next


class LinkedLists():
    """
    This class creates linked lists


    """

    def __init__(self, head=None):
        """
        this is intialized the Linked list

        Args:
            head ([any]): [Insert string or data etc]
        """
        self.head = head

    def __str__(self):
        current = self.head
        st = ''
        while current:
            st += f'{current} -> '
            current = current.get_next()
        return st

    def insert(self, data):
        """
        This function inserts a new data in to the linked lists. Time complexity is O(1) which is fast

        Args:
            data ([any]): [Insert string or data etc]
        """
        new_node = Node(data)
        new_node.set_next(self.head)
        self.head = new_node

    def includes(self, data):
        """
        this function checks to see if a data is in the linked lists and return boolean. The time complexity is O(n)

        Args:
            data ([any]): [as long as the data type is in the list it will return true]
        """

        found = False
        current = self.head

        while current and found is False:
            if current.get_data() == data:
                found = True
            else:
                current = current.get_next()
        if current is None:
            return False

        return found


link_list = LinkedLists()
