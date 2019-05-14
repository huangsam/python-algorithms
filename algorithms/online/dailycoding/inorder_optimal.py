def rightmost(node):
    prev = None
    cur = node
    while cur:
        prev = cur
        cur = cur.right
    return prev


def inorder_optimal(root):
    result = []
    cur = root
    while cur:
        if cur.left:
            left = cur.left
            left_r = rightmost(left)

            # Avoid dead end
            left_r.right = cur

            # Avoid infinite loop
            cur.left = None

            cur = left
        else:
            result.append(cur.value)
            cur = cur.right
    return result
