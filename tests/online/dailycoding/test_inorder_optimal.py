import pytest

from algorithms.collection.tree import TreeNode
from algorithms.online.dailycoding.inorder_optimal import inorder_optimal


@pytest.mark.tree
def test_inorder_optimal_simple():
    """
        1
       / \
      2   3
    """
    r = TreeNode(1)
    r.left = TreeNode(2)
    r.right = TreeNode(3)
    assert [n for n in inorder_optimal(r)] == [2, 1, 3]


@pytest.mark.tree
def test_inorder_optimal_moderate():
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
    assert [n for n in inorder_optimal(r)] == [8, 5, 6, 2, 1, 3]


@pytest.mark.tree
def test_inorder_optimal_symmetric():
    """
            1
           / \
          2   2
         /     \
        3       3
    """
    r = TreeNode(1)
    r.left = TreeNode(2)
    r.left.left = TreeNode(3)
    r.right = TreeNode(2)
    r.right.right = TreeNode(3)
    assert [n for n in inorder_optimal(r)] == [3, 2, 1, 2, 3]
