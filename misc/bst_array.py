class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def create_bst_from_array(arr, left, right):
    """ Create BST from array of integers.
    Args:
        arr (list): List of integer elements.
        left (int): Left boundary.
        right (int): Right boundary.

    Returns:
        TreeNode: Root node of BST.
    """
    if left > right:
        return None
    middle = int((left + right) / 2)
    result = TreeNode(arr[middle])
    result.left = create_bst_from_array(arr, left, middle - 1)
    result.right = create_bst_from_array(arr, middle + 1, right)
    return result


def is_sorted(node, l):
    if node is None:
        return True
    if node.left and node.left.val > node.val:
        return False
    elif node.right and node.right.val < node.val:
        return False
    if not is_sorted(node.left, l) or not is_sorted(node.right, l):
        return False
    return True


def inorder(node):
    if node is None:
        return
    inorder(node.left)
    print(node.val)
    inorder(node.right)


def main():
    for given, expected in [([1], 1),
                            ([1,2,3], 2),
                            ([6,8,10], 8),
                            ([1,2,3,4,5], 3),
                            ([1,2,3,4,5,6,7], 4)]:
        result = create_bst_from_array(given, 0, len(given) - 1)
        assert result.val == expected
        assert is_sorted(result, []) is True
        print("===")
        inorder(result)


if __name__ == '__main__':
    main()
