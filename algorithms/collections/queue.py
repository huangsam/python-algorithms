class Queue:
    """Queue is a FIFO data structure."""

    def __init__(self):
        self.array = []

    def push(self, val):
        """Adds an element to the end of the queue."""
        self.array.append(val)

    def pop(self):
        """Removes and returns the front element of the queue."""
        return self.array.pop(0)

    def size(self):
        """Returns the number of elements in the queue."""
        return len(self.array)


# https://www.geeksforgeeks.org/queue-using-stacks/
class FunkyQueue:
    """Queue made of two stacks."""

    def __init__(self):
        self.s1 = []
        self.s2 = []

    # Optimized for push
    def push(self, val):
        """Adds an element to the queue."""
        self.s1.append(val)

    def pop(self):
        """Removes and returns the front element, or None if empty."""
        if len(self.s1) == 0 and len(self.s2) == 0:
            return None
        if len(self.s2) == 0:
            while len(self.s1) > 0:
                self.s2.append(self.s1.pop())
        return self.s2.pop()

    def size(self):
        """Returns the number of elements in the queue."""
        return len(self.s1) + len(self.s2)
