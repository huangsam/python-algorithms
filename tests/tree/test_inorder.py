import pytest

from algorithms.tree import inorder as in_


@pytest.mark.tree
class TestInorder:
    def test_inorder_iterative(self, simple_tree):
        result = in_.inorder_iterative(simple_tree)
        assert (len(result)) == 6
        assert [1, 3, 2, 5, 4, 6] == result

    def test_inorder_recursive(self, simple_tree):
        result = in_.inorder_recursive(simple_tree)
        assert (len(result)) == 6
        assert [1, 3, 2, 5, 4, 6] == result
