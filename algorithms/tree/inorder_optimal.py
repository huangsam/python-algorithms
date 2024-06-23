from algorithms.collections.tree import TreeNode


def inorder_optimal(root: TreeNode):
    cur: TreeNode | None = root
    while cur:
        if cur.left:
            left = cur.left
            left_r = _rightmost(left)

            # Avoid dead end
            left_r.right = cur

            # Avoid infinite loop
            cur.left = None

            cur = left
        else:
            yield cur.value
            cur = cur.right


def _rightmost(node: TreeNode):
    cur = node
    while cur.right:
        cur = cur.right
    return cur
