class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


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
            result.append(cur.val)
            cur = cur.right
    return result


def main():
    """
    Tree example:

            1
           / \
          2   3
         /
        5
       / \
      8   6
    """
    r = TreeNode(1)
    r.left = TreeNode(2)
    r.left.left = TreeNode(5)
    r.left.left.left = TreeNode(8)
    r.left.left.right = TreeNode(6)
    r.right = TreeNode(3)
    assert inorder_optimal(r) == [8, 5, 6, 2, 1, 3]


if __name__ == '__main__':
    main()
