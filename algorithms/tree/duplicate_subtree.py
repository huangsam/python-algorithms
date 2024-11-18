# https://www.geeksforgeeks.org/check-binary-tree-contains-duplicate-subtrees-size-2/
from algorithms.collections.tree import TreeNode


def duplicate_subtree(root: TreeNode) -> bool:
    _, _, answer = _duplicate_subtree_work(root)
    return answer


def _duplicate_subtree_work(root: TreeNode | None) -> tuple[str, set, bool]:
    if root is None:
        return "", set(), False

    left_post, left_seen, left_dup = _duplicate_subtree_work(root.left)
    right_post, right_seen, right_dup = _duplicate_subtree_work(root.right)

    cur_seq = left_post + right_post + str(root.value)
    seen = left_seen.union(right_seen) | {cur_seq}
    is_duplicate = left_dup or right_dup or any(len(post_seq) > 1 for post_seq in left_seen & right_seen)

    return cur_seq, seen, is_duplicate
