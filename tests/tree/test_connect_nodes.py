import pytest

from algorithms.tree.connect_nodes import NextNode, connect_nodes_double, connect_nodes_single


@pytest.mark.tree
@pytest.mark.parametrize("func", [connect_nodes_double, connect_nodes_single])
def test_connect_nodes(func):
    root = NextNode(1)
    root.left = NextNode(2)
    root.right = NextNode(3)
    root.left.left = NextNode(4)
    root.right.left = NextNode(5)
    root.right.right = NextNode(6)
    func(root)
    assert root.left.next is root.right
    assert root.right.next is None
    assert root.left.left.next is root.right.left
    assert root.right.left.next is root.right.right
    assert root.right.right.next is None
