import pytest

from algorithms.collections.tree import TreeNode
from algorithms.online.codesignal.traverseTree import traverseTree


@pytest.mark.online
def test_traverseTree():
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    result = traverseTree(root)
    assert result == [1, 2, 3]
