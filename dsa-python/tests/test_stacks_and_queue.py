from challenges.stack_and_queues.stack_and_queues import Node, Stack, Queue

import sys


def test_push():
    new_stack = Stack()
    new_stack.push(5)
    assert new_stack.top.data == 5


def test_push_multi():
    new_stack = Stack()
    new_stack.push(5)
    new_stack.push(4)
    new_stack.push(1)
    assert new_stack.top.data == 1
    assert new_stack.top.next_node.data == 4


def test_pop():
    new_stack = Stack()
    new_stack.push(5)
    new_stack.push(4)
    new_stack.push(1)
    new_stack.pop()
    assert new_stack.top.data == 4


def test_pop_multi():
    new_stack = Stack()
    new_stack.push(5)
    new_stack.push(4)
    new_stack.push(1)
    new_stack.pop()
    new_stack.pop()
    assert new_stack.top.data == 5


def test_peek():
    new_stack = Stack()
    new_stack.push(5)
    new_stack.push(4)
    assert new_stack.peek() == 4


def test_empty():
    new_stack = Stack()
    assert new_stack.is_empty() == True


# def test_exception():
#     new_stack = Stack()
#     assert new_stack.pop() == 'Stack is empty'
#     assert new_stack.peek() == 'Stack is empty'


def test_enqueue():
    new_queue = Queue()
    new_queue.enqueue(5)
    assert new_queue.front.data == 5


# Can successfully enqueue multiple values into a queue
def test_enqueue_mult():
    new_queue = Queue()
    new_queue.enqueue(5)
    new_queue.enqueue(4)
    new_queue.enqueue(3)
    new_queue.enqueue(1)
    assert new_queue.front.data == 1
# Can successfully dequeue out of a queue the expected value
# Can successfully peek into a queue, seeing the expected value
# Can successfully empty a queue after multiple dequeues
# Can successfully instantiate an empty queue
# Calling dequeue or peek on empty queue raises exception
