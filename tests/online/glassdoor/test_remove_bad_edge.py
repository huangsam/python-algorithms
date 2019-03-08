import pytest

from collection.tree import TreeNode
from online.glassdoor.remove_bad_edge import remove_bad_edge


@pytest.mark.tree
class TestRemoveBadEdge(object):
    def test_remove_bad_edge(self):
        root = TreeNode(6)
        root.left = TreeNode(3)
        root.right = TreeNode(8)
        root.left.left = TreeNode(2)
        root.left.left.right = TreeNode(8)
        remove_bad_edge(root)
        assert root.right is None
