import pytest

from algorithms.collection.tree import TreeNode


@pytest.mark.tree
def test_root():
    root = TreeNode(1)
    assert root.value == 1
    assert root.left is None
    assert root.right is None


@pytest.mark.tree
def test_children():
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    assert root.left.value == 2
    assert root.right.value == 3
