import pytest

from algorithms.collection.tree import TreeNode
from algorithms.online.cake.is_balanced import is_balanced, is_balanced_optimal


@pytest.mark.tree
def test_is_balanced():
    root = TreeNode(1)
    root.insert_left(2)
    root.insert_right(3)
    root.left.insert_left(4)
    root.left.insert_right(5)
    assert is_balanced(root) is True


@pytest.mark.tree
def test_is_balanced_optimal_good():
    root = TreeNode(1)
    root.insert_left(2)
    root.insert_right(3)
    root.left.insert_left(4)
    root.left.insert_right(5)
    balanced, _ = is_balanced_optimal(root)
    assert balanced is True


@pytest.mark.tree
def test_is_balanced_optimal_bad():
    root = TreeNode(1)
    root.insert_left(2)
    root.left.insert_right(5)
    balanced, _ = is_balanced_optimal(root)
    assert balanced is False
