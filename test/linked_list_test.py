"""Defines unit tests for linked_list.py"""
from src.linked_list import (
    Node,
    LinkedList
)
import pytest


def test_size():
    list_1 = LinkedList()
    list_2 = LinkedList("apple")
    list_3 = LinkedList("apple")
    node_1 = Node("blueberry")
    list_3.front.next = node_1

    assert list_1.size() == 0
    assert list_2.size() == 1
    assert list_3.size() == 2

def test_is_empty():
    list_1 = LinkedList()
    list_2 = LinkedList("apple")

    assert list_1.is_empty() is True
    assert list_2.is_empty() is False

def test_get():
    list_1 = LinkedList("apple")
    list_2 = LinkedList("apple")
    node_1 = Node("blueberry")
    list_2.front.next = node_1

    assert list_1.get(0) == "apple"
    assert list_2.get(0) == "apple"
    assert list_2.get(1) == "blueberry"