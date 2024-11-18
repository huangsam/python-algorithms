import pytest

from algorithms.tree.postorder import postorder_iterative, postorder_recursive


@pytest.mark.tree
def test_postorder_iterative(simple_tree):
    result = postorder_iterative(simple_tree)
    assert (len(result)) == 6
    assert [3, 5, 6, 4, 2, 1] == result


@pytest.mark.tree
def test_postorder_recursive(simple_tree):
    result = postorder_recursive(simple_tree)
    assert (len(result)) == 6
    assert [3, 5, 6, 4, 2, 1] == result
