def get_max(node):
    while node.right:
        node = node.right
    return node.val


def get_min(node):
    while node.left:
        node = node.left
    return node.val


def is_bst(node):
    if node is None:
        return True
    if node.left:
        left_max = get_max(node.left)
        if left_max > node.val:
            return False
        elif node.left.val > node.val:
            return False
        elif is_bst(node.left) is False:
            return False
    if node.right:
        right_min = get_min(node.right)
        if right_min < node.val:
            return False
        elif node.right.val < node.val:
            return False
        elif is_bst(node.right) is False:
            return False
    return True
