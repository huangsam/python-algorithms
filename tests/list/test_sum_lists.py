import pytest

from algorithms.list import sum_lists as slist
from tests.helpers import int_to_list


def _verify(a, b):
    first = int_to_list(a)
    second = int_to_list(b)
    l1 = slist.sum_lists(first, second)
    l2 = int_to_list(a + b)
    while l1 and l2:
        assert l1.value == l2.value
        l1 = l1.next_node
        l2 = l2.next_node
    assert l1 is None
    assert l2 is None


@pytest.mark.math
@pytest.mark.stack
@pytest.mark.list
@pytest.mark.parametrize(
    "a, b",
    [
        (563, 842),
        (1, 999),
        (34, 80),
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
def test_sum_list(a, b):
    _verify(a, b)
