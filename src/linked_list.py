"""Defines the state and behavior for a linked list abstract data type"""

class Node:

    def __init__(self, data, next=None):
        self.data = data
        self.next = next

class LinkedList:

    def __init__(self, data=None):
        self.front = data

    def size(self):
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

    def remove(self, idx):
        if ((idx < 0) or (idx > (self.size()-1))):
            raise IndexError
        if idx == 0:
            val = self.front.data
            self.front = self.front.next
        else:
            curr = self.front
            count = 0
            while count < (idx-1):
                curr = curr.next
                count += 1
            val = curr.next.data
            curr.next = curr.next.next
        return val
