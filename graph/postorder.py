def postorder_recursive(root):
    if root is None:
        return []
    result = postorder_recursive(root.left)
    result.extend(postorder_recursive(root.right))
    result.append(root.val)
    return result
