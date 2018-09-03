def preorder_recursive(root):
    if root is None:
        return []
    result = [root.val]
    result.extend(preorder_recursive(root.left))
    result.extend(preorder_recursive(root.right))
    return result


def preorder_iterative(root):
    visited = []
    c = root
    s = []
    while c is not None or len(s) > 0:
        while c is not None:
            if c.val not in visited:
                visited.append(c.val)
            s.append(c)
            c = c.left
        c = s.pop()
        c = c.right
    return visited
