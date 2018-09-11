from collection.list import ListNode
from online.cake.has_cycle import has_cycle


class TestCakeThief(object):

    def test_has_cycle(self):
        root = ListNode(5)
        root.next_node = root
        assert has_cycle(root) is True

    def test_has_no_cycle(self):
        root = ListNode(5)
        assert has_cycle(root) is False
