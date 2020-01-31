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
        elif target < self.value and self.left == None:
            return False
        elif target > self.value and self.right == None:
            return False
        elif target < self.value and self.left:
            return self.left.contains(target)
        elif target > self.value and self.right:
            return self.right.contains(target)
