from challenges.queue_with_stacks.queue_with_stacks import PseudoQueue
import pytest


def test_pseudo():
    pseudo = PseudoQueue()
    pseudo.enqueue(5)
    pseudo.enqueue(3)
    pseudo.enqueue(2)
    pseudo.enqueue(1)
    pseudo.enqueue(8)
    assert pseudo.dequeue() == 5


def test_multi_dequeue():
    pseudo = PseudoQueue()
    pseudo.enqueue(5)
    pseudo.enqueue(3)
    pseudo.enqueue(2)
    pseudo.enqueue(1)
    pseudo.enqueue(8)
    pseudo.dequeue()
    pseudo.dequeue()
    assert pseudo.dequeue() == 2


def test_empty():
    pseudo = PseudoQueue()
    with pytest.raises(Exception) as e_info:
        pseudo.dequeue()
