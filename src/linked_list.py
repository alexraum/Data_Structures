"""Defines state and behavior for a linked list"""

class Node:

    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:

    def __init__(self, data=None):
        self.front = Node(data)

    def size(self):
        if self.front.data == None:
            return 0
        count = 1
        curr = self.front
        while curr.next is not None:
            count += 1
            curr = curr.next
        return count

    def is_empty(self):
        return self.size() == 0
