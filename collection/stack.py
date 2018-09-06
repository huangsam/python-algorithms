class Stack(object):
    """Stack is a LIFO data structure."""

    def __init__(self):
        self.array = []
        self.maxval = []

    def max(self):
        if len(self.maxval) == 0:
            raise ValueError('No entries have been added')
        return self.maxval[-1]

    def push(self, val):
        self.array.append(val)
        if len(self.maxval) == 0 or self.maxval[-1] <= val:
            self.maxval.append(val)

    def pop(self):
        val = self.array.pop()
        if len(self.maxval) > 0 and self.maxval[-1] == val:
            self.maxval.pop()
        return val

    def size(self):
        return len(self.array)
