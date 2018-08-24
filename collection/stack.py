class Stack(object):
    """Stack is a LIFO data structure."""

    def __init__(self):
        self.array = []

    def push(self, val):
        self.array.append(val)

    def pop(self):
        return self.array.pop()

    def size(self):
        return len(self.array)
