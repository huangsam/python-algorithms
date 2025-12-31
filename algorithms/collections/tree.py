from typing import Any


class TreeNode:
    """Binary tree node has a value and node references."""

    def __init__(self, value: Any):
        self.value: Any = value
        self.left: TreeNode | None = None
        self.right: TreeNode | None = None

    def __lt__(self, other):
        """Compares nodes by value."""
        return self.value < other.value

    def insert_left(self, value):
        """Inserts a left child with the given value."""
        self.left = TreeNode(value)
        return self.left

    def insert_right(self, value):
        """Inserts a right child with the given value."""
        self.right = TreeNode(value)
        return self.right
