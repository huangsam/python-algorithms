import pytest

from collection.tree import TreeNode
from online.geeks.is_bst import is_bst, is_bst_optimal


@pytest.mark.tree
class TestIsBST(object):
    @pytest.mark.parametrize("func", [is_bst, is_bst_optimal])
    def test_is_bst_good_basic(self, func):
        root = TreeNode(2)
        root.left = TreeNode(1)
        root.right = TreeNode(4)
        root.right.left = TreeNode(3)
        root.right.right = TreeNode(5)
        assert func(root) is True

    @pytest.mark.parametrize("func", [is_bst, is_bst_optimal])
    def test_is_bst_good_empty(self, func):
        root = None
        assert func(root) is True

    @pytest.mark.parametrize("func", [is_bst, is_bst_optimal])
    def test_is_bst_bad_basic(self, func):
        root = TreeNode(2)
        root.left = TreeNode(1)
        root.right = TreeNode(4)
        root.right.left = TreeNode(6)
        root.right.right = TreeNode(5)
        assert func(root) is False

    @pytest.mark.parametrize("func", [is_bst, is_bst_optimal])
    def test_is_bst_bad_left(self, func):
        root = TreeNode(2)
        root.left = TreeNode(1)
        root.left.right = TreeNode(5)
        root.left.right.left = TreeNode(3)
        root.left.right.right = TreeNode(7)
        assert func(root) is False

    @pytest.mark.parametrize("func", [is_bst, is_bst_optimal])
    def test_is_bst_bad_right(self, func):
        root = TreeNode(2)
        root.right = TreeNode(4)
        root.right.left = TreeNode(3)
        root.right.left.left = TreeNode(1)
        assert func(root) is False
