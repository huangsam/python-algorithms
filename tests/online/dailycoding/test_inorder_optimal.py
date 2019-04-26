import pytest

from collection.tree import TreeNode
from online.dailycoding.inorder_optimal import inorder_optimal


@pytest.mark.tree
class TestInorderOptimal:
    def test_inorder_optimal_simple(self):
        """
            1
           / \
          2   3
        """
        r = TreeNode(1)
        r.left = TreeNode(2)
        r.right = TreeNode(3)
        assert inorder_optimal(r) == [2, 1, 3]

    def test_inorder_optimal_moderate(self):
        """
                1
               / \
              2   3
             /
            5
           / \
          8   6
        """
        r = TreeNode(1)
        r.left = TreeNode(2)
        r.left.left = TreeNode(5)
        r.left.left.left = TreeNode(8)
        r.left.left.right = TreeNode(6)
        r.right = TreeNode(3)
        assert inorder_optimal(r) == [8, 5, 6, 2, 1, 3]
