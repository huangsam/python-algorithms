def postorder_recursive(root):
    if root is None:
        return []
    result = postorder_recursive(root.left)
    result.extend(postorder_recursive(root.right))
    result.append(root.val)
    return result


# https://www.geeksforgeeks.org/iterative-postorder-traversal/
def postorder_iterative(root):
    fs = []
    ss = []
    visited = []
    if root:
        fs.append(root)
    while len(fs) > 0:
        node = fs.pop()
        ss.append(node)
        if node.left is not None:
            fs.append(node.left)
        if node.right is not None:
            fs.append(node.right)
    while len(ss) > 0:
        visited.append(ss.pop().val)
    return visited
