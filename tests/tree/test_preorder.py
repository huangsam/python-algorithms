import pytest

from algorithms.tree import preorder as pre_


@pytest.mark.tree
class TestPreorder:
    def test_preorder_iterative(self, simple_tree):
        result = pre_.preorder_iterative(simple_tree)
        assert (len(result)) == 6
        assert "1,2,3,4,5,6" == ",".join(map(str, result))

    def test_preorder_recursive(self, simple_tree):
        result = pre_.preorder_recursive(simple_tree)
        assert (len(result)) == 6
        assert "1,2,3,4,5,6" == ",".join(map(str, result))
