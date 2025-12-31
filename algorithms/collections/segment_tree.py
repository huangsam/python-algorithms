class SegmentTree:
    def __init__(self, arr: list[int]) -> None:
        self.n = len(arr)
        self.tree = [0] * (4 * self.n)
        self.build(arr, 0, 0, self.n - 1)

    def build(self, arr: list[int], node: int, start: int, end: int) -> None:
        if start == end:
            self.tree[node] = arr[start]
            return
        mid = (start + end) // 2
        self.build(arr, 2 * node + 1, start, mid)
        self.build(arr, 2 * node + 2, mid + 1, end)
        self.tree[node] = self.tree[2 * node + 1] + self.tree[2 * node + 2]

    def update(self, node: int, start: int, end: int, idx: int, val: int) -> None:
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
        if right < start or end < left:
            return 0
        if left <= start and end <= right:
            return self.tree[node]
        mid = (start + end) // 2
        left = self.query(2 * node + 1, start, mid, left, right)
        right = self.query(2 * node + 2, mid + 1, end, left, right)
        return left + right

    def update_val(self, idx: int, val: int) -> None:
        self.update(0, 0, self.n - 1, idx, val)

    def query_range(self, left: int, right: int) -> int:
        return self.query(0, 0, self.n - 1, left, right)
