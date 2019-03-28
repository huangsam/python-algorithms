import pytest

from graph.inorder import inorder_recursive
from online.geeks.bst_array import create_bst_from_array
from online.geeks.is_bst import is_bst


@pytest.mark.array
@pytest.mark.tree
class TestBSTArray:
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
    def test_create_bst_from_array(self, given, expected):
        root = create_bst_from_array(given, 0, len(given) - 1)
        assert root.val == expected
        assert is_bst(root) is True
        visited = inorder_recursive(root)
        assert len(visited) == len(given)
        for v, g in zip(visited, given):
            assert v == g
