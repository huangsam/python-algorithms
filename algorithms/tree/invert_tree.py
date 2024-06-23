from algorithms.collections.tree import TreeNode


def invert_tree(root: TreeNode | None):
    if not root:
        return
    invert_tree(root.left)
    invert_tree(root.right)
    root.left, root.right = root.right, root.left
