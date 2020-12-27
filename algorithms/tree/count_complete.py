from typing import Optional

from algorithms.collections.tree import TreeNode


def count_complete(root: Optional[TreeNode]):
    if root is None:
        return 0
    left_c = _count_left(root)
    right_c = _count_right(root)
    if left_c == right_c:
        return 2 ** left_c - 1
    return 1 + count_complete(root.left) + count_complete(root.right)


def _count_left(node: TreeNode):
    height = 1
    while node.left:
        node = node.left
        height += 1
    return height


def _count_right(node: TreeNode):
    height = 1
    while node.right:
        node = node.right
        height += 1
    return height
