#
# Definition for binary tree:
# class Tree(object):
#   def __init__(self, x):
#     self.value = x
#     self.left = None
#     self.right = None
from collections import defaultdict


def mostFrequentBookKeep(t, mapping):
    if t is None:
        return 0
    if t.left is None and t.right is None:
        mapping[t.value] += 1
        if mapping["max"] < mapping[t.value]:
            mapping["max"] = mapping[t.value]
        return t.value
    left_sum = mostFrequentBookKeep(t.left, mapping)
    right_sum = mostFrequentBookKeep(t.right, mapping)
    cur_sum = left_sum + right_sum + t.value
    mapping[cur_sum] += 1
    if mapping["max"] < mapping[cur_sum]:
        mapping["max"] = mapping[cur_sum]
    return cur_sum


def mostFrequentSum(t):
    mapping = defaultdict(int)
    mapping["max"] = -1
    mostFrequentBookKeep(t, mapping)
    max_tally = mapping.pop("max")
    result = []
    for s, c in mapping.items():
        if c == max_tally:
            result.append(s)
    return sorted(result)
