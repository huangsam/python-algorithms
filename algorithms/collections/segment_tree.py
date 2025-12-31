class SegmentTree:
    """A segment tree for range sum queries and point updates.

    A segment tree is a data structure that allows efficient range queries and updates on an array.
    It divides the array into segments and stores them in a tree structure, enabling operations like
    summing a range of elements or updating a single element in O(log n) time. This implementation
    supports range sum queries and point updates, making it useful for problems involving frequent
    range aggregations and modifications.
    """

    def __init__(self, arr: list[int]) -> None:
        """Initializes the segment tree with the given array."""
        # N represents the size of the input array
        self.n = len(arr)

        # The segment tree array can be up to 4 times the size of the input array
        # so that we have enough space to store all segments, given that 4xN is
        # a safe boundary for a complete binary tree
        self.tree = [0] * (4 * self.n)

        # Build the segment tree
        self.build(arr, 0, 0, self.n - 1)

    def build(self, arr: list[int], node: int, start: int, end: int) -> None:
        """Builds the segment tree recursively."""
        # Base case: leaf node
        if start == end:
            self.tree[node] = arr[start]
            return

        # Build left and right subtrees
        mid = (start + end) // 2
        self.build(arr, 2 * node + 1, start, mid)
        self.build(arr, 2 * node + 2, mid + 1, end)

        # Internal node will have the sum of both of its children
        self.tree[node] = self.tree[2 * node + 1] + self.tree[2 * node + 2]

    def update(self, node: int, start: int, end: int, idx: int, val: int) -> None:
        """Updates the value at index idx to val."""
        # Base case: leaf node
        if start == end:
            self.tree[node] = val
            return

        # Recurse to the appropriate child
        mid = (start + end) // 2
        if idx <= mid:
            self.update(2 * node + 1, start, mid, idx, val)
        else:
            self.update(2 * node + 2, mid + 1, end, idx, val)

        # Update internal node
        self.tree[node] = self.tree[2 * node + 1] + self.tree[2 * node + 2]

    def query(self, node: int, start: int, end: int, left: int, right: int) -> int:
        """Queries the sum in range [left, right]."""
        # No overlap
        if right < start or end < left:
            return 0

        # Total overlap
        if left <= start and end <= right:
            return self.tree[node]

        # Partial overlap
        mid = (start + end) // 2
        p_left = self.query(2 * node + 1, start, mid, left, right)
        p_right = self.query(2 * node + 2, mid + 1, end, left, right)

        # Combine results
        return p_left + p_right

    def update_val(self, idx: int, val: int) -> None:
        """Updates the value at index idx to val."""
        self.update(0, 0, self.n - 1, idx, val)

    def query_range(self, left: int, right: int) -> int:
        """Queries the sum in range [left, right]."""
        return self.query(0, 0, self.n - 1, left, right)
