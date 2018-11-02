import pytest

from online.glassdoor.remove_every_other import remove_every_other


@pytest.mark.list
class TestRemoveEveryOther(object):

    @staticmethod
    def _add_loop(l):
        prev = None
        cur = l
        while cur:
            prev = cur
            cur = cur.next_node
        prev.next_node = l

    def test_remove_every_other(self, sorted_list):
        self._add_loop(sorted_list)
        remove_every_other(sorted_list)
        cur = sorted_list
        while cur:
            assert cur.value % 2 == 0
            cur = cur.next_node
            if cur is sorted_list:
                return
