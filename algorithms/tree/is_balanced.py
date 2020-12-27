from typing import Optional

from algorithms.collections.tree import TreeNode


def _depth(root: Optional[TreeNode]):
    if root is None:
        return 0
    return 1 + max(_depth(root.left), _depth(root.right))


def is_balanced(root: Optional[TreeNode]):
    if root is None:
        return True
    left_depth = _depth(root.left)
    right_depth = _depth(root.right)
    return (
        abs(left_depth - right_depth) <= 1
        and is_balanced(root.left)
        and is_balanced(root.right)
    )


def is_balanced_optimal(root: Optional[TreeNode]):
    if root is None:
        return (True, 0)
    left_b, left_h = is_balanced_optimal(root.left)
    right_b, right_h = is_balanced_optimal(root.right)
    height = 1 + max(left_h, right_h)
    h_diff = abs(left_h - right_h)
    if h_diff > 1 or left_b is False or right_b is False:
        return (False, -1)
    return (True, height)
