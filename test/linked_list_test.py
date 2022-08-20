"""Defines unit tests for linked_list.py"""
from src.linked_list import (
    Node,
    LinkedList
)


def test_size():
    l1 = LinkedList()
    l2 = LinkedList("apple")
    l3 = LinkedList("apple")
    n2 = Node("blueberry")
    l3.front.next = n2

    assert l1.size() == 0
    assert l2.size() == 1
    assert l3.size() == 2

def test_is_empty():
    l1 = LinkedList()
    l2 = LinkedList("apple")

    assert l1.is_empty() is True
    assert l2.is_empty() is False
