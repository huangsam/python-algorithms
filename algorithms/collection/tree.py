class TreeNode:
    """Binary tree has two children and an associated value."""

    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.next = None

    def insert_left(self, val):
        self.left = TreeNode(val)
        return self.left

    def insert_right(self, val):
        self.right = TreeNode(val)
        return self.right
