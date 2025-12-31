class Stack:
    """Stack is a LIFO data structure."""

    def __init__(self):
        self.array = []
        self.maxval = []

    def max(self):
        """Returns the maximum value in the stack."""
        if len(self.maxval) == 0:
            raise ValueError("No entries have been added")
        return self.maxval[-1]

    def push(self, val):
        """Pushes a value onto the stack."""
        self.array.append(val)
        if len(self.maxval) == 0 or self.maxval[-1] <= val:
            self.maxval.append(val)

    def pop(self):
        """Pops and returns the top value from the stack."""
        val = self.array.pop()
        if len(self.maxval) > 0 and self.maxval[-1] == val:
            self.maxval.pop()
        return val

    def size(self):
        """Returns the number of elements in the stack."""
        return len(self.array)


# https://www.geeksforgeeks.org/implement-stack-using-queue/
class FunkyStack:
    """Stack made of two queues."""

    def __init__(self):
        self.q1 = []
        self.q2 = []

    # Optimized for push
    def push(self, val):
        """Pushes a value onto the stack."""
        self.q1.append(val)

    def pop(self):
        """Pops and returns the top value, or None if empty."""
        if len(self.q1) == 0 and len(self.q2) == 0:
            return None
        while len(self.q1) > 1:
            self.q2.insert(0, self.q1.pop(0))
        val = self.q1.pop(0)
        self.q1, self.q2 = self.q2, self.q1
        return val

    def size(self):
        """Returns the number of elements in the stack."""
        return len(self.q1) + len(self.q2)
