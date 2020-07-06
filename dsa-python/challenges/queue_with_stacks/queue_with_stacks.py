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
        self.stack_one.append(data)

    def dequeue(self):
        if len(self.stack_two) == 0:
            if len(self.stack_one) == 0:
                raise IndexError("Empty queue")
            while len(self.stack_two) > 0:
                last_item_one = self.stack_one.pop()
                self.stack_two.append(last_item_one)
        return self.stack_two.pop()
