from random import randint

import pytest

from algorithms.collections.graph import DirectedGraph
from algorithms.collections.list import ListNode
from algorithms.collections.tree import TreeNode
from algorithms.collections.trie import Trie


@pytest.fixture(scope="function", params=[50, 100, 400])
def array(request) -> list[int]:
    return [randint(0, 100) for i in range(request.param)]


@pytest.fixture(scope="function", params=[50, 100, 400])
def sorted_list(request) -> ListNode:
    """
    1 -> 2 -> 3 -> ... -> n
    """
    head = ListNode(0)
    node = head
    for i in range(1, request.param):
        node.next_node = ListNode(i)
        node = node.next_node
    return head


@pytest.fixture(scope="function")
def simple_tree(request) -> TreeNode:
    """
       1
        \
         2
        / \
       3   4
          / \
         5   6
    """
    root = TreeNode(1)
    root.right = TreeNode(2)
    root.right.left = TreeNode(3)
    root.right.right = TreeNode(4)
    root.right.right.left = TreeNode(5)
    root.right.right.right = TreeNode(6)
    return root


@pytest.fixture(scope="function")
def acyclic_digraph(request) -> DirectedGraph:
    graph = DirectedGraph(("a", "b"), ("a", "c"), ("b", "d"), ("c", "e"))
    return graph


@pytest.fixture(scope="function")
def simple_trie() -> Trie:
    tr = Trie()
    tr.insert("hello")
    tr.insert("hat")
    tr.insert("cat")
    return tr
