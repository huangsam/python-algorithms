# https://www.geeksforgeeks.org/circular-linked-list/
def has_cycle(head):
    slow, fast = head, head
    while slow and fast.next_node and fast.next_node.next_node:
        slow = slow.next_node
        fast = fast.next_node.next_node
        if slow is fast:
            return True
    return False
