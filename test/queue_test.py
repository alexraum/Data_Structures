"""Defines unit tests for the queue abstract data type"""
from src.queue import (
    Queue
)


def test_size():
    queue_1 = Queue()
    queue_2 = Queue()
    queue_2.enqueue("apple")
    queue_2.enqueue("blueberry")

    assert queue_1.size() == 0
    assert queue_2.size() == 2

def test_is_empty():
    queue_1 = Queue()
    queue_2 = Queue()
    queue_2.enqueue("apple")

    assert queue_1.is_empty() is True
    assert queue_2.is_empty() is False

def test_enqueue():
    queue = Queue()
    queue.enqueue("apple")

    assert queue.size() == 1

def test_first():
    queue = Queue()
    queue.enqueue("apple")
    queue.enqueue("blueberry")
    queue.enqueue("cherry")

    assert queue.first() == "apple"

def test_dequeue():
    queue = Queue()
    queue.enqueue("apple")
    queue.enqueue("blueberry")
    queue.enqueue("cherry")

    assert queue.dequeue() == "apple"
    assert queue.size() == 2
