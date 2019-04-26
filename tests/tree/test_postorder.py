import pytest

from algorithms.tree import postorder as post_


@pytest.mark.tree
class TestPostorder:
    def test_postorder_iterative(self, simple_tree):
        result = post_.postorder_iterative(simple_tree)
        assert (len(result)) == 6
        assert "3,5,6,4,2,1" == ",".join(map(str, result))

    def test_postorder_recursive(self, simple_tree):
        result = post_.postorder_recursive(simple_tree)
        assert (len(result)) == 6
        assert "3,5,6,4,2,1" == ",".join(map(str, result))
