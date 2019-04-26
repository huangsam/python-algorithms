import pytest

from algorithms.collection.tree import TreeNode
from algorithms.online.geeks.connect_nodes import (
    connect_nodes_single,
    connect_nodes_double,
)


@pytest.mark.tree
class TestConnectNodes:
    @pytest.mark.parametrize("func", [connect_nodes_double, connect_nodes_single])
    def test_connect_nodes(self, func):
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.right = TreeNode(3)
        root.left.left = TreeNode(4)
        root.right.left = TreeNode(5)
        root.right.right = TreeNode(6)
        func(root)
        assert root.left.next is root.right
        assert root.right.next is None
        assert root.left.left.next is root.right.left
        assert root.right.left.next is root.right.right
        assert root.right.right.next is None
