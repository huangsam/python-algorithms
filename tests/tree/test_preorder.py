import pytest

from algorithms.tree import preorder as _pre


@pytest.mark.tree
def test_preorder_iterative(simple_tree):
    result = _pre.preorder_iterative(simple_tree)
    assert (len(result)) == 6
    assert [1, 2, 3, 4, 5, 6] == result


@pytest.mark.tree
def test_preorder_recursive(simple_tree):
    result = _pre.preorder_recursive(simple_tree)
    assert (len(result)) == 6
    assert [1, 2, 3, 4, 5, 6] == result
