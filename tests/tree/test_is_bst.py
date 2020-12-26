import pytest

from algorithms.collections.tree import TreeNode
from algorithms.tree.is_bst import is_bst, is_bst_optimal


@pytest.mark.tree
@pytest.mark.parametrize("func", [is_bst, is_bst_optimal])
def test_is_bst_good_basic(func):
    root = TreeNode(2)
    root.left = TreeNode(1)
    root.right = TreeNode(4)
    root.right.left = TreeNode(3)
    root.right.right = TreeNode(5)
    assert func(root) is True


@pytest.mark.tree
@pytest.mark.parametrize("func", [is_bst, is_bst_optimal])
def test_is_bst_good_empty(func):
    root = None
    assert func(root) is True


@pytest.mark.tree
@pytest.mark.parametrize("func", [is_bst, is_bst_optimal])
def test_is_bst_bad_basic(func):
    root = TreeNode(2)
    root.left = TreeNode(1)
    root.right = TreeNode(4)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(5)
    assert func(root) is False


@pytest.mark.tree
@pytest.mark.parametrize("func", [is_bst, is_bst_optimal])
def test_is_bst_bad_left(func):
    root = TreeNode(2)
    root.left = TreeNode(1)
    root.left.right = TreeNode(5)
    root.left.right.left = TreeNode(3)
    root.left.right.right = TreeNode(7)
    assert func(root) is False


@pytest.mark.tree
@pytest.mark.parametrize("func", [is_bst, is_bst_optimal])
def test_is_bst_bad_right(func):
    root = TreeNode(2)
    root.right = TreeNode(4)
    root.right.left = TreeNode(3)
    root.right.left.left = TreeNode(1)
    assert func(root) is False
