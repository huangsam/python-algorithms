import pytest

from algorithms.collection.tree import TreeNode
from algorithms.tree.remove_bad_edge import remove_bad_edge


@pytest.mark.tree
def test_remove_bad_edge():
    root = TreeNode(6)
    root.left = TreeNode(3)
    root.right = TreeNode(8)
    root.left.left = TreeNode(2)
    root.left.left.right = TreeNode(8)
    remove_bad_edge(root)
    assert root.right is None
