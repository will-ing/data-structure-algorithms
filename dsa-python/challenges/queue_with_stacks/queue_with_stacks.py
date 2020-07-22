# import does not work
# from challenges.stack_and_queues.stack_and_queues import Node


class PseudoQueue:
    """
    implement our standard queue interface
    """

    def __init__(self):
        self.first_stack = []
        self.second_stack = []

    def enqueue(self, data):
        """
        Adds element to the stack

        Args:
            data ([type]): [Any value]
        """
        self.first_stack.append(data)

    def dequeue(self):
        """
        moves stack 1 to stack 2 and pops off the end

        Raises:
            IndexError: [will return if queue is empty]

        Returns:
            [value]: [Return FIFO]
        """
        if len(self.second_stack) == 0:
            if len(self.first_stack) == 0:
                raise IndexError("Empty queue")
            while len(self.first_stack) > 0:
                last_item_one = self.first_stack.pop()
                self.second_stack.append(last_item_one)
        return self.second_stack.pop()
