from dll_queue import Queue # do I need either of these?
from dll_stack import Stack

class Binary_Search_Tree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

# insert
    def insert(self, value):
        if self.value is None:
            self.value = value
        if value < self.value:
            if self.left is None:
                self.left = Binary_Search_Tree(value)
            else:
                self.left.insert(value)
        else:
            if self.right is None:
                self.right = Binary_Search_Tree(value)
            else:
                self.right.insert(value)

# boolean, True if exists, else False
    def contains(self, target):
        if self.value == target:
            return True
        elif target < self.value:
            return self.left.contains(target) if self.left is not None else False
        else:
            return self.right.contains(target) is self.right is not None else False
