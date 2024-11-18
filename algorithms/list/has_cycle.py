from algorithms.collections.list import ListNode


# https://www.geeksforgeeks.org/circular-linked-list/
def has_cycle(head: ListNode):
    slow: ListNode | None = head
    fast: ListNode | None = head
    while slow and fast and fast.next_node:
        slow = slow.next_node
        fast = fast.next_node.next_node
        if slow is fast:
            return True
    return False
