import pytest

from collection.tree import TreeNode
from online.geeks.duplicate_subtree import duplicate_subtree


@pytest.mark.tree
class TestDuplicateSubtree(object):

    def test_duplicate_subtree(self):
        root = TreeNode('A')
        root.left = TreeNode('B')
        root.left.left = TreeNode('D')
        root.left.right = TreeNode('E')
        root.right = TreeNode('C')
        root.right.right = TreeNode('B')
        root.right.right.left = TreeNode('D')
        root.right.right.right = TreeNode('E')
        assert duplicate_subtree(root) is True

    def test_duplicate_subtree_empty(self):
        root = None
        assert duplicate_subtree(root) is False
