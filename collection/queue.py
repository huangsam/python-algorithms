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


class FunkyQueue(object):
    """Queue made of two stacks."""

    def __init__(self):
        self.s1 = []
        self.s2 = []

    def push(self, val):
        raise NotImplementedError('Not implemented at this level')

    def pop(self):
        raise NotImplementedError('Not implemented at this level')
