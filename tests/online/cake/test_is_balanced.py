from collection.tree import TreeNode
from online.cake.is_balanced import is_balanced


class TestIsBalanced(object):

    def test_is_balanced(self):
        root = TreeNode(6)
        root.insert_left(3)
        root.insert_right(4)
        root.left.insert_left(2)
        root.left.insert_right(7)
        assert is_balanced(root) is True

    def test_is_balanced_optimal_good(self):
        root = TreeNode(6)
        root.insert_left(3)
        root.insert_right(4)
        root.left.insert_left(2)
        root.left.insert_right(7)
        balanced, _ = is_balanced_optimal(root)
        assert balanced is True

    def test_is_balanced_optimal_bad(self):
        root = TreeNode(6)
        root.insert_left(3)
        root.left.insert_right(7)
        balanced, _ = is_balanced_optimal(root)
        assert balanced is False
