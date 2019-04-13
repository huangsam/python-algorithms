def count_complete(root):
    if root is None:
        return 0
    left_c = count_left(root)
    right_c = count_right(root)
    if left_c == right_c:
        return 2 ** left_c - 1
    else:
        return 1 + count_complete(root.left) + count_complete(root.right)


def count_left(node):
    if not node:
        return 0
    height = 0
    while node:
        node = node.left
        height += 1
    return height


def count_right(node):
    if not node:
        return 0
    height = 0
    while node:
        node = node.right
        height += 1
    return height
