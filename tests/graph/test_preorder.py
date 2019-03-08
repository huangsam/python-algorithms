import pytest

from graph.preorder import preorder_iterative, preorder_recursive


@pytest.mark.tree
class TestPreorder(object):
    def test_preorder_iterative(self, simple_tree):
        result = preorder_iterative(simple_tree)
        assert (len(result)) == 6
        assert "1,2,3,4,5,6" == ",".join(map(str, result))

    def test_preorder_recursive(self, simple_tree):
        result = preorder_recursive(simple_tree)
        assert (len(result)) == 6
        assert "1,2,3,4,5,6" == ",".join(map(str, result))
