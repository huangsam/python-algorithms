import math


class SegmentNode:
    """A node in the segment tree holding multiple aggregate values."""

    def __init__(self, sum_val: int = 0, min_val: float = float("inf"), max_val: float = float("-inf"), gcd_val: int = 0) -> None:
        self.sum_val = sum_val
        self.min_val = min_val
        self.max_val = max_val
        self.gcd_val = gcd_val


class SegmentTree:
    """A segment tree for range queries (sum, min, max, gcd) and point updates.

    This implementation uses a node-based structure where each node stores
    sum, min, max, and gcd values for efficient range queries.
    """

    def __init__(self, arr: list[int]) -> None:
        """Initializes the segment tree with the given array."""
        self.n = len(arr)
        self.tree: list[SegmentNode] = [SegmentNode() for _ in range(4 * self.n)]
        self.build(arr, 0, 0, self.n - 1)

    def build(self, arr: list[int], node: int, start: int, end: int) -> None:
        """Builds the segment tree recursively."""
        if start == end:
            # Leaf node setup
            self.tree[node] = SegmentNode(arr[start], arr[start], arr[start], arr[start])
            return

        mid = (start + end) // 2
        self.build(arr, 2 * node + 1, start, mid)
        self.build(arr, 2 * node + 2, mid + 1, end)

        left = self.tree[2 * node + 1]
        right = self.tree[2 * node + 2]
        self.tree[node] = SegmentNode(
            left.sum_val + right.sum_val, min(left.min_val, right.min_val), max(left.max_val, right.max_val), math.gcd(left.gcd_val, right.gcd_val)
        )

    def update(self, node: int, start: int, end: int, idx: int, val: int) -> None:
        """Updates the value at index idx to val."""
        if start == end:
            # Leaf node update
            self.tree[node] = SegmentNode(val, val, val, val)
            return

        mid = (start + end) // 2
        if idx <= mid:
            self.update(2 * node + 1, start, mid, idx, val)
        else:
            self.update(2 * node + 2, mid + 1, end, idx, val)

        left = self.tree[2 * node + 1]
        right = self.tree[2 * node + 2]
        self.tree[node] = SegmentNode(
            left.sum_val + right.sum_val, min(left.min_val, right.min_val), max(left.max_val, right.max_val), math.gcd(left.gcd_val, right.gcd_val)
        )

    def query(self, node: int, start: int, end: int, left: int, right: int) -> SegmentNode:
        """Queries the range [left, right] and returns a SegmentNode with combined values."""
        if right < start or end < left:
            # No overlap: return neutral elements
            return SegmentNode(0, float("inf"), float("-inf"), 0)

        if left <= start and end <= right:
            # Total overlap
            return SegmentNode(self.tree[node].sum_val, self.tree[node].min_val, self.tree[node].max_val, self.tree[node].gcd_val)

        # Partial overlap
        mid = (start + end) // 2
        p_left = self.query(2 * node + 1, start, mid, left, right)
        p_right = self.query(2 * node + 2, mid + 1, end, left, right)

        return SegmentNode(
            p_left.sum_val + p_right.sum_val,
            min(p_left.min_val, p_right.min_val),
            max(p_left.max_val, p_right.max_val),
            math.gcd(p_left.gcd_val, p_right.gcd_val),
        )

    def update_val(self, idx: int, val: int) -> None:
        """Updates the value at index idx to val."""
        self.update(0, 0, self.n - 1, idx, val)

    def query_range(self, left: int, right: int) -> SegmentNode:
        """Queries the range [left, right] and returns a SegmentNode with sum, min, max, gcd."""
        return self.query(0, 0, self.n - 1, left, right)
