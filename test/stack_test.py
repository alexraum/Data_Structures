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

    assert stack_1.is_empty() == True
    assert stack_2.is_empty() == False
