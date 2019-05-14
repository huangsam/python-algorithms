import math


def is_bst(node):
    if node is None:
        return True
    if node.left and get_max(node.left) > node.value:
        return False
    if node.right and get_min(node.right) < node.value:
        return False
    return is_bst(node.left) and is_bst(node.right)


def get_max(node):
    while node.right:
        node = node.right
    return node.value


def get_min(node):
    while node.left:
        node = node.left
    return node.value


# https://www.geeksforgeeks.org/a-program-to-check-if-a-binary-tree-is-bst-or-not/
def is_bst_optimal(node):
    return is_bst_util(node, -math.inf, math.inf)


def is_bst_util(node, min_val, max_val):
    if node is None:
        return True
    if node.value < min_val or node.value > max_val:
        return False
    return is_bst_util(node.left, min_val, node.value - 1) and is_bst_util(
        node.right, node.value + 1, max_val
    )
