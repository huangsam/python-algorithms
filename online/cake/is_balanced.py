def depth(root):
    if root is None:
        return 0
    return 1 + max(depth(root.left), depth(root.right))


def is_balanced(root):
    if root is None:
        return True
    left_depth = depth(root.left)
    right_depth = depth(root.right)
    return abs(left_depth - right_depth) <= 1 \
        and is_balanced(root.left) \
        and is_balanced(root.right)
