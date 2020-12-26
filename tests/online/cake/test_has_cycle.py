import pytest

from algorithms.collection.list import ListNode
from algorithms.online.cake.has_cycle import has_cycle


@pytest.mark.list
def test_has_cycle_root():
    root = ListNode(0)
    root.next_node = root
    assert has_cycle(root) is True


@pytest.mark.list
def test_has_cycle_non_root():
    root = ListNode(0)
    root.next_node = ListNode(1)
    root.next_node.next_node = root
    assert has_cycle(root) is True


@pytest.mark.list
def test_has_no_cycle(sorted_list):
    assert has_cycle(sorted_list) is False
