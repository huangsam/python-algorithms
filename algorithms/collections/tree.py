from typing import Any


class TreeNode:
    """Binary tree node has a value and node references.

    A node in a binary tree, holding a value and references to left and right child nodes. This structure
    forms the basis for binary tree algorithms, supporting recursive traversals and tree manipulations.
    It includes methods for inserting children and comparing nodes by value.
    """

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
