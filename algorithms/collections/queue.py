class Queue:
    """Queue is a FIFO data structure.

    A first-in, first-out (FIFO) data structure implemented using a list. Elements are added to the end
    and removed from the front, making it suitable for breadth-first search and other queue-based algorithms.
    It provides basic operations like push, pop, and size checking.
    """

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
    """Queue made of two stacks.

    An implementation of a queue using two stacks, optimized for push operations. This approach uses one
    stack for enqueueing and another for dequeueing, providing amortized O(1) time for both operations.
    It's an educational example of implementing a queue with stacks.
    """

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
