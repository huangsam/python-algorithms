class TreeNode:
    """Binary tree has two children and an associated value."""

    def __init__(self, x):
        self.value = x
        self.left = None
        self.right = None
        self.next = None

    def insert_left(self, value):
        self.left = TreeNode(value)
        return self.left

    def insert_right(self, value):
        self.right = TreeNode(value)
        return self.right
