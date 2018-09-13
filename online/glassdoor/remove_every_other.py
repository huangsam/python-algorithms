def remove_every_other(head):
    toggle = False
    prev = None
    cur = head
    traversed_head = 0

    while True:
        if cur == head:
            traversed_head += 1
            if traversed_head == 2:
                return

        if toggle is True and cur != head:
            prev.next_node = cur.next_node

        toggle ^= True

        prev = cur
        cur = cur.next_node
