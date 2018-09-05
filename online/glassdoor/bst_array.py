class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def create_bst_from_array(arr, left, right):
    """Create BST from array of integers.
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


def is_sorted(node):
    if node is None:
        return (None, True)
    left_value, left_sorted = is_sorted(node.left)
    if (left_sorted is False) or (left_value and left_value > node.val):
        return (None, False)
    right_value, right_sorted = is_sorted(node.right)
    if (right_sorted is False) or (right_value is not None and right_value < node.val):
        return (None, False)
    return (node.val, True)


def inorder(node):
    if node is None:
        return
    inorder(node.left)
    print(node.val)
    inorder(node.right)


def main():
    for given, expected in [
            ([1], 1),
            ([1, 2, 3], 2),
            ([6, 8, 10], 8),
            ([1, 2, 3, 4, 5], 3),
            ([1, 2, 3, 4, 5, 6, 7], 4)]:
        root = create_bst_from_array(given, 0, len(given) - 1)
        assert root.val == expected
        val, flag = is_sorted(root)
        assert val == root.val
        assert flag is True
        print('===')
        inorder(root)


if __name__ == '__main__':
    main()
