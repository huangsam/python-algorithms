import pytest

from collection.tree import TreeNode


@pytest.mark.tree
class TestTree:
    def test_root(self):
        root = TreeNode(1)
        assert root.val == 1
        assert root.left is None
        assert root.right is None

    def test_children(self):
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.right = TreeNode(3)
        assert root.left.val == 2
        assert root.right.val == 3
