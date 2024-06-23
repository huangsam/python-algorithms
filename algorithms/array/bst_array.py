from algorithms.collections.tree import TreeNode


# https://www.geeksforgeeks.org/sorted-array-to-balanced-bst/
def create_bst_from_array(arr: list[int], left: int, right: int) -> TreeNode | None:
    if left > right:
        return None
    middle = (left + right) // 2
    result = TreeNode(arr[middle])
    result.left = create_bst_from_array(arr, left, middle - 1)
    result.right = create_bst_from_array(arr, middle + 1, right)
    return result
