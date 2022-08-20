"""Defines unit tests for linked_list.py"""
from src.linked_list import (
    Node,
    LinkedList
)
import pytest


def test_size():
    list_1 = LinkedList()
    list_2 = LinkedList(Node("apple"))
    list_3 = LinkedList(Node("apple"))
    list_3.add(list_3.size(), "blueberry")

    assert list_1.size() == 0
    assert list_2.size() == 1
    assert list_3.size() == 2

def test_is_empty():
    list_1 = LinkedList()
    list_2 = LinkedList(Node("apple"))

    assert list_1.is_empty() is True
    assert list_2.is_empty() is False

def test_get():
    list_1 = LinkedList(Node("apple"))
    list_2 = LinkedList(Node("apple"))
    list_2.add(list_2.size(), "cherry")
    list_2.add(list_2.size()-1, "blueberry")

    assert list_1.get(0) == "apple"
    assert list_2.get(0) == "apple"
    assert list_2.get(list_2.size()-2) == "blueberry"
    assert list_2.get(list_2.size()-1) == "cherry"

def test_set():
    list_1 = LinkedList(Node("apple"))
    list_2 = LinkedList(Node("apple"))
    list_2.add(list_2.size(), "blueberry")

    list_1.set(0, "orange")
    list_2.set(0, "banana")
    list_2.set(list_2.size()-1, "strawberry")

    assert list_1.get(0) == "orange"
    assert list_2.get(0) == "banana"
    assert list_2.get(list_2.size()-1) == "strawberry"

def test_add():
    list_1 = LinkedList()
    list_1.add(0, "apple")
    list_2 = LinkedList(Node("cherry"))
    list_2.add(0, "apple")
    list_2.add(2, "dragonfruit")
    list_2.add(1, "blueberry")

    assert list_1.get(0) == "apple"
    assert list_2.get(0) == "apple"
    assert list_2.get(1) == "blueberry"
    assert list_2.get(2) == "cherry"
    assert list_2.get(list_2.size()-1) == "dragonfruit"

def test_remove():
    list_1 = LinkedList(Node("apple"))
    list_1.add(1, "blueberry")
    list_1.add(2, "cherry")
    list_1.add(3, "dragonfruit")
    list_1.add(4, "fig")

    assert list_1.remove(0) == "apple"
    assert list_1.remove(1) == "cherry"
    assert list_1.remove(list_1.size()-1) == "fig"
    assert list_1.remove(0) == "blueberry"
    assert list_1.remove(list_1.size()-1) == "dragonfruit"
