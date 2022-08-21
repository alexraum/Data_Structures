"""Defines the state and behavior for a stack abstract data type"""
import src.linked_list as list

class Stack():

    def __init__(self):
        self.linked_list = list.LinkedList()

    def size(self):
        return self.linked_list.size()

    def is_empty(self):
        return self.linked_list.is_empty()

    def peek(self):
        return self.linked_list.get(self.linked_list.size()-1)

    def push(self, elem):
        self.linked_list.add(self.linked_list.size(), elem)

    def pop(self):
        return self.linked_list.remove(self.linked_list.size()-1)
