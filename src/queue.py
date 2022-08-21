"""Defines the state and behavior for a queue abstract data type"""
import src.linked_list as list

class Queue():
    
    def __init__(self):
        self.linked_list = list.LinkedList()

    def size(self):
        return self.linked_list.size()

    def is_empty(self):
        return self.linked_list.is_empty()

    
