# import does not work
# from challenges.stack_and_queues.stack_and_queues import Node


class PseudoQueue:
    """
    implement our standard queue interface
    """

    def __init__(self):
        self.stack_one = []
        self.stack_two = []

    def enqueue(self, data):
        """
        Adds element to the stack

        Args:
            data ([type]): [Any value]
        """
        self.stack_one.append(data)

    def dequeue(self):
        """
        moves stack 1 to stack 2 and pops off the end

        Raises:
            IndexError: [will return if queue is empty]

        Returns:
            [value]: [Return FIFO]
        """
        if len(self.stack_two) == 0:
            if len(self.stack_one) == 0:
                raise IndexError("Empty queue")
            while len(self.stack_one) > 0:
                last_item_one = self.stack_one.pop()
                self.stack_two.append(last_item_one)
        return self.stack_two.pop()
