class Queue:
    """Queue is a FIFO data structure."""

    def __init__(self):
        self.array = []

    def push(self, val):
        self.array.append(val)

    def pop(self):
        return self.array.pop(0)

    def size(self):
        return len(self.array)


class FunkyQueue:
    """Queue made of two stacks."""

    def __init__(self):
        self.s1 = []
        self.s2 = []

    # Optimized for push
    def push(self, val):
        self.s1.append(val)

    def pop(self):
        if len(self.s1) == 0 and len(self.s2) == 0:
            return None
        if len(self.s2) == 0:
            while len(self.s1) > 0:
                self.s2.append(self.s1.pop())
        return self.s2.pop()

    def size(self):
        return len(self.s1) + len(self.s2)
