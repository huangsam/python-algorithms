import pytest

from algorithms.collections.list import ListNode
from algorithms.list.reverse_alt_k import reverse_alt_k


@pytest.mark.list
@pytest.mark.parametrize(
    "k, size, expected",
    [
        (3, 6, [3, 2, 1, 4, 5, 6]),
        (3, 9, [3, 2, 1, 4, 5, 6, 9, 8, 7]),
        (2, 6, [2, 1, 3, 4, 6, 5]),
        (2, 5, [2, 1, 3, 4, 5]),
    ],
)
def test_reverse_alt_k(k: int, size: int, expected: list[int]):
    head = ListNode(1)
    node: ListNode | None = head
    for i in range(2, size + 1):
        assert node is not None
        node.next_node = ListNode(i)
        node = node.next_node

    new_head = reverse_alt_k(head, k)

    node = new_head
    actual = []
    while node:
        actual.append(node.value)
        node = node.next_node

    assert actual == expected
