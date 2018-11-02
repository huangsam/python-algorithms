import pytest

from collection.tree import TreeNode
from online.cake.is_balanced import (
    is_balanced,
    is_balanced_optimal,
)


@pytest.mark.tree
class TestIsBalanced(object):

    def test_is_balanced(self):
        root = TreeNode(1)
        root.insert_left(2)
        root.insert_right(3)
        root.left.insert_left(4)
        root.left.insert_right(5)
        assert is_balanced(root) is True

    def test_is_balanced_optimal_good(self):
        root = TreeNode(1)
        root.insert_left(2)
        root.insert_right(3)
        root.left.insert_left(4)
        root.left.insert_right(5)
        balanced, _ = is_balanced_optimal(root)
        assert balanced is True

    def test_is_balanced_optimal_bad(self):
        root = TreeNode(1)
        root.insert_left(2)
        root.left.insert_right(5)
        balanced, _ = is_balanced_optimal(root)
        assert balanced is False
