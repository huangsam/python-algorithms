import pytest

from algorithms.collections.tree import TreeNode
from algorithms.online.codesignal.hasPathWithGivenSum import hasPathWithGivenSum


@pytest.mark.online
def test_hasPathWithGivenSum():
    # Tree: 1 -> 2, 3
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    assert hasPathWithGivenSum(root, 3) is True  # 1+2
    assert hasPathWithGivenSum(root, 4) is True  # 1+3
    assert hasPathWithGivenSum(root, 5) is False
