def preorder_recursive(root):
    if root is None:
        return []
    result = [root.val]
    result.extend(preorder_recursive(root.left))
    result.extend(preorder_recursive(root.right))
    return result


# https://www.geeksforgeeks.org/iterative-preorder-traversal/
def preorder_iterative(root):
    visited = []
    s = [root]
    while len(s) > 0:
        c = s.pop()
        visited.append(c.val)
        if c.right is not None:
            s.append(c.right)
        if c.left is not None:
            s.append(c.left)
    return visited
