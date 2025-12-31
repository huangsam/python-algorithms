import pytest

from algorithms.collections.tree import TreeNode
from algorithms.tree.remove_bad_edge import remove_bad_edge


@pytest.mark.tree
def test_remove_bad_edge():
    root = TreeNode(6)
    root.left = TreeNode(3)
    root.right = TreeNode(8)
    root.left.left = TreeNode(2)
    root.left.left.right = root.right
    remove_bad_edge(root)
    assert root.right is None


@pytest.mark.tree
def test_remove_bad_edge_right():
    root = TreeNode(6)
    root.right = TreeNode(8)
    root.right.right = TreeNode(9)
    root.right.right.left = root  # cycle
    remove_bad_edge(root)
    assert root.right.right.left is None
