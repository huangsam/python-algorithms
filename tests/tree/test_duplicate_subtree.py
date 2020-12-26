import pytest

from algorithms.collection.tree import TreeNode
from algorithms.tree.duplicate_subtree import duplicate_subtree


@pytest.mark.tree
def test_duplicate_subtree():
    root = TreeNode("A")
    root.left = TreeNode("B")
    root.left.left = TreeNode("D")
    root.left.right = TreeNode("E")
    root.right = TreeNode("C")
    root.right.right = TreeNode("B")
    root.right.right.left = TreeNode("D")
    root.right.right.right = TreeNode("E")
    assert duplicate_subtree(root) is True


@pytest.mark.tree
def test_duplicate_subtree_empty():
    root = None
    assert duplicate_subtree(root) is False
