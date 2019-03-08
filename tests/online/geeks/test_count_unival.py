import pytest

from collection.tree import TreeNode
from online.geeks.count_unival import count_unival


@pytest.mark.tree
class TestCountUnival(object):
    def test_count_unival_full(self):
        root = TreeNode(0)
        root.left = TreeNode(1)
        root.right = TreeNode(0)
        root.right.left = TreeNode(1)
        root.right.right = TreeNode(0)
        root.right.left.left = TreeNode(1)
        root.right.left.right = TreeNode(1)
        assert count_unival(root) == 5

    def test_count_unival_partial_1(self):
        root = TreeNode(0)
        root.left = TreeNode(1)
        root.left.left = TreeNode(1)
        root.right = TreeNode(0)
        root.right.left = TreeNode(1)
        root.right.right = TreeNode(0)
        root.right.left.left = TreeNode(1)
        root.right.left.right = TreeNode(1)
        assert count_unival(root) == 6

    def test_count_unival_partial_2(self):
        root = TreeNode(5)
        root.left = TreeNode(5)
        root.left.left = TreeNode(5)
        root.right = TreeNode(5)
        root.right.right = TreeNode(5)
        assert count_unival(root) == 5
