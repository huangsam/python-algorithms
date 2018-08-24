#
# Definition for binary tree:
# class Tree(object):
#   def __init__(self, x):
#     self.value = x
#     self.left = None
#     self.right = None


def isMirror(l, r):
    if l is None and r is None:
        return True
    if l and r and l.value == r.value:
        return isMirror(l.left, r.right) and isMirror(l.right, r.left)
    return False


def isTreeSymmetric(t):
    if t is None:
        return True
    return isMirror(t.left, t.right)
