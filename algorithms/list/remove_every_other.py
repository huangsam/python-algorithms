from algorithms.collections.list import ListNode


def remove_every_other(head: ListNode):
    is_other = False
    prev: ListNode | None = None
    cur: ListNode | None = head
    head_passed_count = 0

    while True:
        if cur is head:
            head_passed_count += 1
            if head_passed_count == 2:
                return

        if is_other and cur and prev and cur is not head:
            prev.next_node = cur.next_node

        is_other ^= True

        prev = cur
        if cur:
            cur = cur.next_node
