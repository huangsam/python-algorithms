def count_unival(root):
    _, count = count_unival_work(root)
    return count


# https://www.geeksforgeeks.org/find-count-of-singly-subtrees/
def count_unival_work(root):
    if root is None:
        return (True, 0)
    elif root.left is None and root.right is None:
        return (True, 1)
    l_flag, l_count = count_unival_work(root.left)
    r_flag, r_count = count_unival_work(root.right)
    total_count = l_count + r_count
    total_flag = l_flag & r_flag
    if root.left and root.right:
        total_flag &= (root.left.val == root.right.val)
    if total_flag is True:
        total_count += 1
    return total_flag, total_count
