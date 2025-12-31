from typing import Any


class ListNode:
    """Linked list node has a value and node references."""

    def __init__(self, value: Any):
        self.value = value
        self.next_node: ListNode | None = None
        self.prev_node: ListNode | None = None

    def __lt__(self, other):
        return self.value < other.value


def list_size(lst: ListNode):
    """Get size of list node."""
    size = 1
    while lst.next_node:
        lst = lst.next_node
        size += 1
    return size
