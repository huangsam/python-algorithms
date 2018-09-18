import pytest

from collection.list import ListNode
from online.geeks.reverse_alt_k import reverse_alt_k


class TestReverseList(object):

    @pytest.mark.parametrize('k, size, expected', [
        (3, 6, [3, 2, 1, 4, 5, 6]),
        (3, 9, [3, 2, 1, 4, 5, 6, 9, 8, 7]),
        (2, 6, [2, 1, 3, 4, 6, 5]),
        (2, 5, [2, 1, 3, 4, 5]),
    ])
    def test_reverse_alt_k(self, k, size, expected):
        head = ListNode(1)
        node = head
        for i in range(2, size + 1):
            node.next_node = ListNode(i)
            node = node.next_node
        nhead = reverse_alt_k(head, k)
        result = []
        node = nhead
        i = 0
        while node:
            expected[i] = node.value
            node = node.next_node
            i += 1
