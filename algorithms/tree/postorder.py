from typing import Optional

from algorithms.collections.tree import TreeNode


def postorder_recursive(root: Optional[TreeNode]):
    if root is None:
        return []
    result = postorder_recursive(root.left)
    result.extend(postorder_recursive(root.right))
    result.append(root.value)
    return result


# https://www.geeksforgeeks.org/iterative-postorder-traversal/
def postorder_iterative(root: TreeNode):
    stack = [root]
    scanned = []
    while len(stack) > 0:
        c = stack.pop()
        scanned.append(c.value)
        if c.left is not None:
            stack.append(c.left)
        if c.right is not None:
            stack.append(c.right)
    return scanned[::-1]
