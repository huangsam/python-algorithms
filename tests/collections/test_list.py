import pytest

from algorithms.collections.list import ListNode


@pytest.mark.list
def test_list_is_sorted(sorted_list):
    prev_node = None
    cur_node = sorted_list
    while cur_node:
        if prev_node:
            assert cur_node.value > prev_node.value
        prev_node = cur_node
        cur_node = cur_node.next_node


@pytest.mark.list
def test_list_is_unsorted(sorted_list):
    prev_node = None
    cur_node = ListNode(99)
    cur_node.next_node = sorted_list
    is_unsorted = False
    while cur_node:
        if prev_node:
            is_unsorted = True
        prev_node = cur_node
        cur_node = cur_node.next_node
    assert is_unsorted
