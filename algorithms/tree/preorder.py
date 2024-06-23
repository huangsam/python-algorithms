from algorithms.collections.tree import TreeNode


def preorder_recursive(root: TreeNode | None):
    if root is None:
        return []
    result = [root.value]
    result.extend(preorder_recursive(root.left))
    result.extend(preorder_recursive(root.right))
    return result


# https://www.geeksforgeeks.org/iterative-preorder-traversal/
def preorder_iterative(root: TreeNode):
    visited = []
    s = [root]
    while len(s) > 0:
        c = s.pop(0)
        visited.append(c.value)
        if c.left is not None:
            s.append(c.left)
        if c.right is not None:
            s.append(c.right)
    return visited
