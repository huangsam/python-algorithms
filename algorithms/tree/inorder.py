from collections import deque
from typing import Deque, List, Optional

from algorithms.collections.tree import TreeNode


def inorder_recursive(root: Optional[TreeNode]):
    if root is None:
        return []
    result = inorder_recursive(root.left)
    result.append(root.value)
    result.extend(inorder_recursive(root.right))
    return result


# https://www.geeksforgeeks.org/inorder-tree-traversal-without-recursion/
def inorder_iterative(root: TreeNode):
    visited: List[TreeNode] = []
    c: Optional[TreeNode] = root
    s: Deque[TreeNode] = deque()
    while c is not None or len(s) > 0:
        while c is not None:
            s.append(c)
            c = c.left
        c = s.pop()
        visited.append(c.value)
        c = c.right
    return visited
