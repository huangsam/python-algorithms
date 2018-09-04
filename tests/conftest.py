from random import randint

import pytest

from collection.list import ListNode
from collection.tree import TreeNode


@pytest.fixture(scope='function', params=[50, 100, 400])
def array(request):
    return [randint(0, 100) for i in range(request.param)]


@pytest.fixture(scope='function', params=[50, 100, 400])
def sorted_list(request):
    """
    1 -> 2 -> 3 -> ... -> n
    """
    head = ListNode(0)
    node = head
    for i in range(1, request.param):
        node.next_node = ListNode(i)
        node = node.next_node
    return head


@pytest.fixture(scope='function')
def simple_tree(request):
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
