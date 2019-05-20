import pytest

from algorithms.collection.list import ListNode
import algorithms.online.geeks.sum_lists as slist


def int_to_list(n):
    """Helper method for test data"""
    tmp = n
    cur = None
    while tmp > 0:
        node = ListNode(tmp % 10)
        node.next = cur
        cur = node
        tmp = tmp // 10
    return cur


@pytest.mark.math
@pytest.mark.stack
@pytest.mark.list
class TestSumLists:
    @staticmethod
    def debug(lst):
        x = ""
        while lst:
            x += f"{lst.value}->"
            lst = lst.next
        print(x[:-2])

    @staticmethod
    def verify(a, b):
        first = int_to_list(a)
        second = int_to_list(b)
        l1 = slist.sum_lists(first, second)
        l2 = int_to_list(a + b)
        while l1 and l2:
            assert l1.value == l2.value
            l1 = l1.next
            l2 = l2.next
        assert l1 is None
        assert l2 is None

    @pytest.mark.parametrize(
        "a, b",
        [
            (563, 842),
            (1, 999),
            (34, 80),
            (1, 0),
            (1, 1),
            (1, 9),
            (11, 9),
            (101, 9),
            (1001, 9),
            (13945, 3913),
            (38137310373, 673461391333339),
            (9999999, 99999999999),
        ],
    )
    def test_sum_list(self, a, b):
        self.verify(a, b)

    def test_sum_list_zero(self):
        first = int_to_list(0)
        second = int_to_list(0)
        assert slist.sum_lists(first, second) is None
