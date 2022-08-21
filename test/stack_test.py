"""Defines unit tests for the stack abstract data type"""
from src.stack import (
    Stack
)


def test_size():
    stack_1 = Stack()
    stack_2 = Stack()
    stack_2.push("apple")
    stack_2.push("blueberry")
    stack_2.push("cherry")

    assert stack_1.size() == 0
    assert stack_2.size() == 3

def test_is_empty():
    stack_1 = Stack()
    stack_2 = Stack()
    stack_2.push("apple")

    assert stack_1.is_empty() is True
    assert stack_2.is_empty() is False

def test_peek():
    stack = Stack()
    stack.push("apple")
    stack.push("pear")
    stack.push("watermelon")

    assert stack.peek() == "watermelon"

def test_push():
    stack = Stack()
    stack.push("lemon")

    assert stack.size() == 1
    assert stack.is_empty() is False
    assert stack.peek() == "lemon"

def test_pop():
    stack = Stack()
    stack.push("peach")
    stack.push("grape")

    assert stack.pop() == "grape"
    assert stack.size() == 1
