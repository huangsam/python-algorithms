import pytest

from algorithms.tree.inorder import inorder_iterative, inorder_recursive


@pytest.mark.tree
def test_inorder_iterative(simple_tree):
    result = inorder_iterative(simple_tree)
    assert (len(result)) == 6
    assert [1, 3, 2, 5, 4, 6] == result


@pytest.mark.tree
def test_inorder_recursive(simple_tree):
    result = inorder_recursive(simple_tree)
    assert (len(result)) == 6
    assert [1, 3, 2, 5, 4, 6] == result
