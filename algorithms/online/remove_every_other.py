def remove_every_other(head):
    toggle = False
    prev = None
    cur = head
    traversed = 0

    while True:
        if cur == head:
            traversed += 1
            if traversed == 2:
                return

        if toggle is True and cur != head:
            prev.next_node = cur.next_node

        toggle ^= True

        prev = cur
        cur = cur.next_node
