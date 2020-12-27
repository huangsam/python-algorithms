import math
from typing import Optional

from algorithms.collections.tree import TreeNode


def is_bst(node: Optional[TreeNode]):
    if node is None:
        return True
    if node.left and _get_max(node.left) > node.value:
        return False
    if node.right and _get_min(node.right) < node.value:
        return False
    return is_bst(node.left) and is_bst(node.right)


def _get_max(node: TreeNode) -> object:
    while node.right:
        node = node.right
    return node.value


def _get_min(node: TreeNode):
    while node.left:
        node = node.left
    return node.value


# https://www.geeksforgeeks.org/a-program-to-check-if-a-binary-tree-is-bst-or-not/
def is_bst_optimal(node: TreeNode):
    return _is_bst_util(node, -math.inf, math.inf)


def _is_bst_util(node: Optional[TreeNode], min_val: float, max_val: float):
    if node is None:
        return True
    if node.value < min_val or node.value > max_val:
        return False
    return _is_bst_util(node.left, min_val, node.value - 1) and _is_bst_util(
        node.right, node.value + 1, max_val
    )
