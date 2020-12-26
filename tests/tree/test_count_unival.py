import pytest

from algorithms.collection.tree import TreeNode
from algorithms.tree.count_unival import count_unival


@pytest.mark.tree
def test_count_unival_full():
    root = TreeNode(0)
    root.left = TreeNode(1)
    root.right = TreeNode(0)
    root.right.left = TreeNode(1)
    root.right.right = TreeNode(0)
    root.right.left.left = TreeNode(1)
    root.right.left.right = TreeNode(1)
    assert count_unival(root) == 5


@pytest.mark.tree
def test_count_unival_partial_1():
    root = TreeNode(0)
    root.left = TreeNode(1)
    root.left.left = TreeNode(1)
    root.right = TreeNode(0)
    root.right.left = TreeNode(1)
    root.right.right = TreeNode(0)
    root.right.left.left = TreeNode(1)
    root.right.left.right = TreeNode(1)
    assert count_unival(root) == 6


@pytest.mark.tree
def test_count_unival_partial_2():
    root = TreeNode(5)
    root.left = TreeNode(5)
    root.left.left = TreeNode(5)
    root.right = TreeNode(5)
    root.right.right = TreeNode(5)
    assert count_unival(root) == 5
