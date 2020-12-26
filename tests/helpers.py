from typing import List

from algorithms.collection.list import ListNode


def is_sorted(array: List):
    """Verify that list is sorted."""
    alen = len(array)
    for i in range(1, alen):
        if array[i - 1] > array[i]:
            return False
    return True


def int_to_list(n: int):
    """Convert integer to list."""
    tmp = n
    cur = None
    while tmp > 0:
        node = ListNode(tmp % 10)
        node.next_node = cur
        cur = node
        tmp = tmp // 10
    return cur


def list_size(lst: ListNode):
    """Get size of list node"""
    size = 0
    while lst is not None:
        lst = lst.next_node
        size += 1
    return size
