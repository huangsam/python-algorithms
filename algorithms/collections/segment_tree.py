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

    We store the segment tree in a list, where the parent-child relationships
    are maintained as follows:

    - For a node at index i:
      - Left child is at index 2*i + 1
      - Right child is at index 2*i + 2
    - The root node is at index 0.
    - The leaf nodes correspond to the elements of the input array.

    The build function constructs the tree in O(n) time, while both update and
    query operations run in O(log n) time, making this structure efficient for
    dynamic array updates and range queries.
    """

    def __init__(self, arr: list[int]) -> None:
        """Initializes the segment tree with the given array."""
        self.n = len(arr)
        self.tree: list[SegmentNode] = [SegmentNode() for _ in range(4 * self.n)]
        self.build(arr, 0, 0, self.n - 1)

    def build(self, arr: list[int], node: int, start: int, end: int) -> None:
        """Builds the segment tree recursively.

        The intuition behind the build function is to construct the segment
        tree in a bottom-up manner. For each node, we calculate the sum,
        minimum, maximum, and gcd values based on its children nodes.
        If the node is a leaf (i.e., start == end), we directly assign
        the values from the input array. For internal nodes, we combine
        the values from the left and right children to compute the
        aggregate values for that node.
        """
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
        """Updates the value at index idx to val.

        The update function is designed to modify the value at a specific index in
        the original array and then update the corresponding nodes in the segment
        tree. The function traverses down the tree to find the leaf node
        corresponding to the index and updates its value. After updating the leaf
        node, it propagates the changes up to the root, ensuring that all
        affected nodes have their aggregate values (sum, min, max, gcd) updated
        accordingly.
        """
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
        """Queries the range [left, right] and returns a SegmentNode with combined values.

        The query function is designed to retrieve the aggregate values
        (sum, min, max, gcd) for a specified range [left, right]. The
        function checks for three types of overlap between the current
        node's range and the query range: no overlap, total overlap,
        and partial overlap. In the case of no overlap, it returns a neutral
        SegmentNode that does not affect the results. For total overlap, it
        returns the values stored in the current node. For partial overlap,
        it recursively queries both the left and right children and combines
        their results to compute the final aggregate values for the specified range.
        """
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
