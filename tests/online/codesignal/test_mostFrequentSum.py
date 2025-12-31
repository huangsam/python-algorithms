import pytest

from algorithms.collections.tree import TreeNode
from algorithms.online.codesignal.mostFrequentSum import mostFrequentSum


@pytest.mark.online
def test_mostFrequentSum():
    # Tree: 1 -> 2, 3
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    result = mostFrequentSum(root)
    assert 2 in result  # leaf 2
    assert 3 in result  # leaf 3
