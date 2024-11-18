import pytest

from algorithms.collections.list import ListNode
from algorithms.list.remove_every_other import remove_every_other


def _add_loop(list_node: ListNode):
    cur = list_node
    while cur.next_node is not None:
        cur = cur.next_node
    cur.next_node = list_node


@pytest.mark.list
def test_remove_every_other(sorted_list_node):
    _add_loop(sorted_list_node)
    remove_every_other(sorted_list_node)
    cur = sorted_list_node
    while cur:
        assert cur.value % 2 == 0
        cur = cur.next_node
        if cur is sorted_list_node:
            return
