from algorithms.collections.tree import TreeNode


def count_unival(root: TreeNode):
    _, count = _count_unival_work(root)
    return count


# https://www.geeksforgeeks.org/find-count-of-singly-subtrees/
def _count_unival_work(root: TreeNode | None):
    if root is None:
        return (True, 0)
    elif root.left is None and root.right is None:
        return (True, 1)
    l_flag, l_count = _count_unival_work(root.left)
    r_flag, r_count = _count_unival_work(root.right)
    total_count = l_count + r_count
    total_flag = l_flag & r_flag
    if root.left and root.right:
        total_flag &= root.left.value == root.right.value
    if total_flag is True:
        total_count += 1
    return total_flag, total_count
