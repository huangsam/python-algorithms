from typing import Any, Optional


class ListNode:
    """Linked list has a value and node references."""

    def __init__(self, value: Any):
        self.value = value
        self.next_node: Optional[ListNode] = None
        self.prev_node: Optional[ListNode] = None

    def __lt__(self, other):
        return self.value < other.value
