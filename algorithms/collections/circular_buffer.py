class CircularBuffer:
    """A fixed-size circular buffer."""

    def __init__(self, capacity: int):
        if capacity <= 0:
            raise ValueError("Capacity must be positive")
        self.capacity = capacity
        self.buffer = [None] * capacity
        self.size = 0
        self.head = 0
        self.tail = 0

    def append(self, item):
        """Add an item to the end of the buffer, overwriting the oldest if full."""
        self.buffer[self.tail] = item
        if self.size == self.capacity:
            self.head = (self.head + 1) % self.capacity
        else:
            self.size += 1
        self.tail = (self.tail + 1) % self.capacity

    def get(self):
        """Remove and return the oldest item from the buffer."""
        if self.size == 0:
            raise IndexError("Buffer is empty")
        item = self.buffer[self.head]
        self.buffer[self.head] = None
        self.head = (self.head + 1) % self.capacity
        self.size -= 1
        return item

    def __len__(self):
        return self.size

    def __getitem__(self, index):
        if index < 0 or index >= self.size:
            raise IndexError("Index out of range")
        return self.buffer[(self.head + index) % self.capacity]

    def to_list(self):
        """Return the buffer as a list in order of insertion."""
        return [self[i] for i in range(self.size)]
