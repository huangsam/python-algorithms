# https://www.geeksforgeeks.org/a-program-to-check-if-a-binary-tree-is-bst-or-not/
def is_bst(node):
    if node is None:
        return True
    if node.left and get_max(node.left) > node.val:
        return False
    if node.right and get_min(node.right) < node.val:
        return False
    return is_bst(node.left) and is_bst(node.right)


def get_max(node):
    while node.right:
        node = node.right
    return node.val


def get_min(node):
    while node.left:
        node = node.left
    return node.val
