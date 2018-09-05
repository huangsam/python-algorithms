def is_bst(node):
    if node is None:
        return (None, True)
    left_value, left_sorted = is_bst(node.left)
    if (left_sorted is False) or (left_value and left_value > node.val):
        return (left_value, False)
    right_value, right_sorted = is_bst(node.right)
    if (right_sorted is False) or (right_value is not None and right_value < node.val):
        return (right_value, False)
    return (node.val, True)
