#
# Definition for binary tree:
# class Tree(object):
#   def __init__(self, x):
#     self.value = x
#     self.left = None
#     self.right = None


def leafSumFound(t, s, prev_val):
    if t is None:
        return False
    cur_val = t.value + prev_val
    if t.left is None and t.right is None:
        return cur_val == s
    left_found = leafSumFound(t.left, s, cur_val)
    right_found = leafSumFound(t.right, s, cur_val)
    return left_found or right_found


def hasPathWithGivenSum(t, s):
    if t is None and s == 0:
        return True
    return leafSumFound(t, s, 0)
