import pytest

from tree.inorder import inorder_iterative, inorder_recursive


@pytest.mark.tree
class TestInorder:
    def test_inorder_iterative(self, simple_tree):
        result = inorder_iterative(simple_tree)
        assert (len(result)) == 6
        assert "1,3,2,5,4,6" == ",".join(map(str, result))

    def test_inorder_recursive(self, simple_tree):
        result = inorder_recursive(simple_tree)
        assert (len(result)) == 6
        assert "1,3,2,5,4,6" == ",".join(map(str, result))
