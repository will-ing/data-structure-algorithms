from linked_list.linked_list import Node


class MergedList:
    """
    Merges linked lists
    """

    def __init__(self, head=None):
        """[summary]

        Args:
            head ([type], optional): [description]. Defaults to None.
        """
        self.head = head

    def __repr__(self):
        return f'{self.head}'

    def merge(self, list_one, list_two):
        """[This takes in two lists and returns the head of the new sorted merged list REF: https://www.youtube.com/watch?v=r3MAkVZkD0s]

        Args:
            list_one (linked_list): [default is set to None]
            list_two (linked_list): [default is set to None]

        Returns:
            head.next: [This is the head of the new merged list]
        """
        head = Node(0)
        ptr = head

        while True:
            if list_one is None and list_two is None:
                break
            elif list_one is None:
                ptr.next = list_two
                break
            elif list_two is None:
                ptr.next = list_one
                break
            else:
                sml_val = 0
                if list_one.data < list_two.data:
                    sml_val = list_one.data
                    list_one = list_one.next_node
                else:
                    sml_val = list_two.data
                    list_two = list_two.next_node

            newNode = Node(sml_val)
            ptr.next = newNode
            ptr = ptr.next_node

        return head.next_node
