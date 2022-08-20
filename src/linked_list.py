"""Defines state and behavior for a linked list"""

class Node:

    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:

    def __init__(self, data=None):
        self.front = Node(data)
