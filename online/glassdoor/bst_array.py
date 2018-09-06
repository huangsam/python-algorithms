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
    middle = (left + right) // 2
    result = TreeNode(arr[middle])
    result.left = create_bst_from_array(arr, left, middle - 1)
    result.right = create_bst_from_array(arr, middle + 1, right)
    return result
