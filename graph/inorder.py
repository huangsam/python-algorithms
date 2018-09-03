def inorder_recursive(root):
    if root is None:
        return []
    result = inorder_recursive(root.left)
    result.append(root.val)
    result.extend(inorder_recursive(root.right))
    return result


def inorder_iterative(root):
    visited = []
    c = root
    s = []
    while c is not None or len(s) > 0:
        while c is not None:
            s.append(c)
            c = c.left
        c = s.pop()
        visited.append(c.val)
        c = c.right
    return visited
