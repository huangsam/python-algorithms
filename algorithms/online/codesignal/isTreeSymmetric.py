#
# Definition for binary tree:
# class Tree:
#   def __init__(self, x):
#     self.value = x
#     self.left = None
#     self.right = None


def isTreeSymmetric(t):
    if t is None:
        return True
    return isMirror(t.left, t.right)


def isMirror(left, right):
    if left is None and right is None:
        return True
    if left and right and left.value == right.value:
        return isMirror(left.left, right.right) and isMirror(left.right, right.left)
    return False
