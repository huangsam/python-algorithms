class Stack(object):
    """Stack is a LIFO data structure."""

    def __init__(self):
        self.array = []
        self.maxval = []

    def max(self):
        if len(self.maxval) == 0:
            raise ValueError("No entries have been added")
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


class FunkyStack(object):
    """Stack made of two queues."""

    def __init__(self):
        self.q1 = []
        self.q2 = []

    # Optimized for push
    def push(self, val):
        self.q1.append(val)

    def pop(self):
        if len(self.q1) == 0 and len(self.q2) == 0:
            return None
        while len(self.q1) > 1:
            self.q2.append(self.q1.pop(0))
        self.q1, self.q2 = self.q2, self.q1
        return self.q2.pop(0)

    def size(self):
        return len(self.q1) + len(self.q2)
