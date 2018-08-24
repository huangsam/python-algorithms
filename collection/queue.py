class Queue(object):
    """Queue is a FIFO data structure."""

    def __init__(self):
        self.array = []

    def push(self, val):
        self.array.append(val)

    def pop(self):
        return self.array.pop(0)

    def size(self):
        return len(self.array)
