from algorithms.collections.list import ListNode


# https://www.geeksforgeeks.org/reverse-alternate-k-nodes-in-a-singly-linked-list/
def reverse_alt_k(head: ListNode | None, k: int):
    if head is None or head.next_node is None:
        return head

    cur: ListNode | None = head
    prev: ListNode | None = None

    # Run reversal
    counter = k
    while counter > 0 and cur:
        nxt = cur.next_node
        cur.next_node = prev
        prev = cur
        cur = nxt
        counter -= 1

    # Set new tail's next pointer
    head.next_node = cur

    # Skip reversal
    counter = k - 1
    while counter > 0 and cur:
        cur = cur.next_node
        counter -= 1

    if cur:
        cur.next_node = reverse_alt_k(cur.next_node, k)

    return prev
