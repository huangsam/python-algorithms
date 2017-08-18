#
# Definition for binary tree:
# class Tree(object):
#   def __init__(self, x):
#     self.value = x
#     self.left = None
#     self.right = None


def traverseTree(t):
    to_visit = []
    result = []
    if t is not None:
        to_visit.append(t)
    while len(to_visit) > 0:
        cur_node = to_visit.pop(0)
        if cur_node is None:
            continue
        to_visit.append(cur_node.left)
        to_visit.append(cur_node.right)
        result.append(cur_node.value)
    return result
