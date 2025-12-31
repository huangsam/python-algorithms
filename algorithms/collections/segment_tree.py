class SegmentTree:
    """A segment tree for range sum queries and point updates."""

    def __init__(self, arr: list[int]) -> None:
        """Initializes the segment tree with the given array."""
        self.n = len(arr)
        self.tree = [0] * (4 * self.n)
        self.build(arr, 0, 0, self.n - 1)

    def build(self, arr: list[int], node: int, start: int, end: int) -> None:
        """Builds the segment tree recursively."""
        if start == end:
            self.tree[node] = arr[start]
            return
        mid = (start + end) // 2
        self.build(arr, 2 * node + 1, start, mid)
        self.build(arr, 2 * node + 2, mid + 1, end)
        self.tree[node] = self.tree[2 * node + 1] + self.tree[2 * node + 2]

    def update(self, node: int, start: int, end: int, idx: int, val: int) -> None:
        """Updates the value at index idx to val."""
        if start == end:
            self.tree[node] = val
            return
        mid = (start + end) // 2
        if idx <= mid:
            self.update(2 * node + 1, start, mid, idx, val)
        else:
            self.update(2 * node + 2, mid + 1, end, idx, val)
        self.tree[node] = self.tree[2 * node + 1] + self.tree[2 * node + 2]

    def query(self, node: int, start: int, end: int, left: int, right: int) -> int:
        """Queries the sum in range [left, right]."""
        if right < start or end < left:
            return 0
        if left <= start and end <= right:
            return self.tree[node]
        mid = (start + end) // 2
        p_left = self.query(2 * node + 1, start, mid, left, right)
        p_right = self.query(2 * node + 2, mid + 1, end, left, right)
        return p_left + p_right

    def update_val(self, idx: int, val: int) -> None:
        """Updates the value at index idx to val."""
        self.update(0, 0, self.n - 1, idx, val)

    def query_range(self, left: int, right: int) -> int:
        """Queries the sum in range [left, right]."""
        return self.query(0, 0, self.n - 1, left, right)
