"""Defines state and behavior for a linked list"""

class Node:

    def __init__(self, data, next=None):
        self.data = data
        self.next = next


class LinkedList:

    def __init__(self, data=None):
        self.front = Node(data)

    def size(self):
        if self.front.data == None:
            return 0
        curr = self.front
        count = 0
        while curr is not None:
            curr = curr.next
            count += 1
        return count

    def is_empty(self):
        return self.size() == 0

    def get(self, idx):
        if ((idx < 0) or (idx > (self.size()-1))):
            raise IndexError
        curr = self.front
        count = 0
        while count != idx:
            curr = curr.next
            count += 1
        return curr.data

    def set(self, idx, elem):
        if ((idx < 0) or (idx > (self.size()-1))):
            raise IndexError
        curr = self.front
        count = 0
        while count != idx:
            curr = curr.next
            count += 1
        curr.data = elem

    def add(self, idx, elem):
        if ((idx < 0) or (idx > (self.size()))):
            raise IndexError
        if idx == 0:
            node = Node(elem, self.front)
            self.front = node
        else:
            curr = self.front
            count = 0
            while count < (idx-1):
                curr = curr.next
                count += 1
            curr.next = Node(elem, curr.next)
