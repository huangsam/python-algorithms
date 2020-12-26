# https://www.geeksforgeeks.org/reverse-a-linked-list/
def reverse_list(ll):
    cur_node = ll
    prev_node = None
    while cur_node:
        next_node = cur_node.next_node
        cur_node.next_node = prev_node
        prev_node = cur_node
        cur_node = next_node
    return prev_node
