from algorithms.collection.list import ListNode


def list_size(lst):
    size = 0
    while lst is not None:
        lst = lst.next
        size += 1
    return size


# https://www.geeksforgeeks.org/sum-of-two-linked-lists/
def sum_lists(l1, l2):
    l1_len = list_size(l1)
    l2_len = list_size(l2)

    # Identify big list and small list
    big_l, small_l = (l1, l2) if l1_len > l2_len else (l2, l1)
    diff = abs(l1_len - l2_len)

    head = tail = None
    tstack = []

    # Step 1: Normalize list lengths
    while diff > 0:
        if tail is None:
            head = tail = ListNode(big_l.value)
        else:
            tail.next = ListNode(big_l.value)
            tail = tail.next
        tstack.append(tail)
        big_l = big_l.next
        diff -= 1

    # Step 2: Prepare stack summing
    astack = []
    while big_l:
        astack.append((big_l.value, small_l.value))
        big_l = big_l.next
        small_l = small_l.next

    # Step 3: Execute stack summing
    carry = 0
    acc = tmp = None
    while len(astack) > 0:
        v1, v2 = astack.pop()
        vsum = v1 + v2 + carry
        carry, leftover = vsum // 10, vsum % 10
        tmp = ListNode(leftover)
        tmp.next = acc
        acc = tmp

    # Step 4: Connect stack sum with unsummed
    if head is None:
        head = acc
    else:
        tail.next = acc

    # Step 5: Handle carry for unsummed
    while len(tstack) > 0:
        tail = tstack.pop()
        if carry == 0:
            break
        tsum = tail.value + carry
        carry, leftover = tsum // 10, tsum % 10
        tail.value = leftover

    # Step 6: Add node to head if carry exists
    if carry == 1:
        tmp = ListNode(1)
        tmp.next = head
        head = tmp

    return head
