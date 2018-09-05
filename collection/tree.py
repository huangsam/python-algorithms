class TreeNode(object):
    """Binary search tree has two children."""

    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    def insert_left(self, val):
        self.left = TreeNode(val)
        return self.left

    def insert_right(self, val):
        self.right = TreeNode(val)
        return self.right
