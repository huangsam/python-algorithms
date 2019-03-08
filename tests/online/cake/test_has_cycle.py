import pytest

from collection.list import ListNode
from online.cake.has_cycle import has_cycle


@pytest.mark.list
class TestHasCycle(object):
    def test_has_cycle_root(self):
        root = ListNode(0)
        root.next_node = root
        assert has_cycle(root) is True

    def test_has_cycle_non_root(self):
        root = ListNode(0)
        root.next_node = ListNode(1)
        root.next_node.next_node = root
        assert has_cycle(root) is True

    def test_has_no_cycle(self, sorted_list):
        assert has_cycle(sorted_list) is False
