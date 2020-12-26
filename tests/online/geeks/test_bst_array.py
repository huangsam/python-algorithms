import pytest

from algorithms.online.geeks.bst_array import create_bst_from_array
from algorithms.online.geeks.is_bst import is_bst
from algorithms.tree.inorder import inorder_recursive


@pytest.mark.array
@pytest.mark.tree
@pytest.mark.parametrize(
    "given, expected",
    [
        ([1], 1),
        ([1, 2, 3], 2),
        ([6, 8, 10], 8),
        ([1, 2, 3, 4, 5], 3),
        ([1, 2, 3, 4, 5, 6, 7], 4),
    ],
)
def test_create_bst_from_array(given, expected):
    root = create_bst_from_array(given, 0, len(given) - 1)
    assert root.value == expected
    assert is_bst(root) is True
    visited = inorder_recursive(root)
    assert len(visited) == len(given)
    for v, g in zip(visited, given):
        assert v == g
