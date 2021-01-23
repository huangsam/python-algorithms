import pytest

from algorithms.collections.tree import TreeNode
from algorithms.tree.inorder import inorder_recursive
from algorithms.tree.invert_tree import invert_tree


@pytest.mark.tree
def test_invert_tree(simple_tree):
    original_inorder = [1, 3, 2, 5, 4, 6]
    assert inorder_recursive(simple_tree) == original_inorder
    invert_tree(simple_tree)
    assert inorder_recursive(simple_tree) == list(reversed(original_inorder))
