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
        new_node.next_node(self.head)
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

    def append_to_end(self, data):
        # ref: https://www.geeksforgeeks.org/linked-list-set-2-inserting-a-node/
        """Appends value to the end of the list

        Args:
            data ([type]): [any value]
        """
        current = self.head
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return

        while (current.next_node):
            current = current.next_node

        current.next_node = new_node

    def insert_after(self, find_data, new_data):
        # ref: https://www.geeksforgeeks.org/linked-list-set-2-inserting-a-node/
        """Insert after a value that is in the list

        Args:
            find_data ([any]): [this value has to exist]\\
            new_data ([type]): [This is the data you want to enter]
        """
        new_node = Node(new_data)

        current = self.head

        while current is not None:
            if current.data == find_data:
                new_node.next_node = current.next_node
                current.next_node = new_node
            current = current.next_node

    def insert_before(self, find_data, new_data):
        """Insert before a value that is in the list

        Args:
            find_data ([any]): [this value has to exist]\\
            new_data ([type]): [This is the data you want to enter]
        """
        new_node = Node(new_data)

        current = self.head

        while current.next_node is not None:
            if current.next_node.data == find_data:
                new_node.next_node = current.next_node
                current.next_node = new_node
                break
            current = current.next_node

    def kth(self, k):
        """Return the value of a index or kth from the end of the list for a value

        Args:
            k ([index]): [enter the index you are inquiring about]

        Returns:
            [value]: [this the value of the index you entered]
        """

        current = self.head
        count = 0
        idx = count - k
        while current is not None:
            count += 1
            current = current.next_node

        current = self.head
        idx = count - k
        for i in range(idx):
            current = current.next_node

        return current.data

    def reverse_list(self):
        prev = None
        current = self.head
        while current != None:
            next_node = current.next_node
            current.next_node = prev
            prev = current
            current = next_node
        self.head = prev
