# https://www.geeksforgeeks.org/check-binary-tree-contains-duplicate-subtrees-size-2/
def duplicate_subtree(root):
    _, _, answer = duplicate_subtree_work(root)
    return answer


def duplicate_subtree_work(root):
    if root is None:
        return '', set(), False

    left_post, left_seen, left_dup = duplicate_subtree_work(root.left)
    right_post, right_seen, right_dup = duplicate_subtree_work(root.right)

    cur_str = left_post + right_post + root.val
    common = [i for i in left_seen.intersection(right_seen) if len(i) > 1]

    is_duplicate = len(common) > 0 or left_dup or right_dup

    seen = left_seen.union(right_seen)
    seen.add(cur_str)

    return cur_str, seen, is_duplicate
