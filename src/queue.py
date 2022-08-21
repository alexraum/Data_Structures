"""Defines the state and behavior for a queue abstract data type"""
import src.linked_list as list

class Queue():
    
    def __init__(self):
        self.linked_list = list.LinkedList()

    def size(self):
        return self.linked_list.size()

    def is_empty(self):
        return self.linked_list.is_empty()

    def enqueue(self, elem):
        self.linked_list.add(self.linked_list.size(), elem)

    def first(self):
        return self.linked_list.get(0)

    def dequeue(self):
        return self.linked_list.remove(0)