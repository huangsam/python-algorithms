from algorithms.collections.list import ListNode, list_size


# https://www.geeksforgeeks.org/sum-of-two-linked-lists/
def sum_lists(l1, l2):
    l1_len = list_size(l1)
    l2_len = list_size(l2)

    # Step 1: Identify big + small lists
    l1_bigger = l1_len > l2_len
    big_l = l1 if l1_bigger else l2
    small_l = l2 if l1_bigger else l1

    # Step 2: Calculate diff between lists
    diff = abs(l1_len - l2_len)

    # Step 3: Trim big list and track its trimmed nodes in reverse order
    head = tail = None
    tstack = []
    while diff > 0:
        if tail is None:
            head = tail = ListNode(big_l.value)
        else:
            tail.next_node = ListNode(big_l.value)
            tail = tail.next_node
        tstack.append(tail)
        big_l = big_l.next_node
        diff -= 1

    # Step 4: Prepare stack sum
    astack = []
    while big_l:
        astack.append((big_l.value, small_l.value))
        big_l = big_l.next_node
        small_l = small_l.next_node

    # Step 5: Execute stack sum
    acc = None
    carry = 0
    while len(astack) > 0:
        v1, v2 = astack.pop()
        vsum = v1 + v2 + carry
        carry, leftover = vsum // 10, vsum % 10
        tmp = ListNode(leftover)
        tmp.next_node = acc
        acc = tmp

    # Step 6: Connect trimmed nodes of big list with summed result
    if head is None:
        head = acc
    else:
        tail.next_node = acc

    # Step 7: Handle carry for trimmed nodes of big list
    while len(tstack) > 0:
        tail = tstack.pop()
        if carry == 0:
            break
        tsum = tail.value + carry
        carry, leftover = tsum // 10, tsum % 10
        tail.value = leftover

    # Step 8: Add node to head if carry exists
    if carry == 1:
        tmp = ListNode(1)
        tmp.next_node = head
        head = tmp

    return head
