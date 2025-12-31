from typing import Any


class ListNode:
    """Linked list node has a value and node references.

    A node in a doubly linked list, containing a value and references to the previous and next nodes.
    This allows for efficient insertion and deletion operations in both directions, making it suitable
    for implementations of linked lists where bidirectional traversal is needed.
    """

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
