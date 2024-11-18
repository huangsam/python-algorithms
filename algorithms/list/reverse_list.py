from algorithms.collections.list import ListNode


# https://www.geeksforgeeks.org/reverse-a-linked-list/
def reverse_list(ll: ListNode):
    cur_node: ListNode | None = ll
    prev_node: ListNode | None = None
    while cur_node:
        next_node = cur_node.next_node
        cur_node.next_node = prev_node
        prev_node = cur_node
        cur_node = next_node
    return prev_node
