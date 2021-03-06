from typing import List

from algorithms.collections.list import ListNode


def is_sorted(array: List):
    """Verify that list is sorted."""
    alen = len(array)
    for i in range(1, alen):
        if array[i - 1] > array[i]:
            return False
    return True


def int_to_list(n: int):
    """Convert integer to list."""
    if n <= 0:
        raise ValueError(f"Invalid number: {n}")
    cur = ListNode(n % 10)
    tmp = n // 10
    while tmp > 0:
        node = ListNode(tmp % 10)
        node.next_node = cur
        cur = node
        tmp = tmp // 10
    return cur
