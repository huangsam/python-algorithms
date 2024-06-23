from typing import Any


class TreeNode:
    """Binary tree node has a value and node references."""

    def __init__(self, value: Any):
        self.value: Any = value
        self.left: TreeNode | None = None
        self.right: TreeNode | None = None

    def __lt__(self, other):
        return self.value < other.value

    def insert_left(self, value):
        self.left = TreeNode(value)
        return self.left

    def insert_right(self, value):
        self.right = TreeNode(value)
        return self.right
