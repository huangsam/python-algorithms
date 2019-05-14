from algorithms.collection.tree import TreeNode


# https://www.geeksforgeeks.org/construct-a-binary-tree-from-postorder-and-inorder/
def create_postorder_inorder(postorder, postrange, inorder, inrange):
    post_left, post_right = postrange
    if post_right - post_left == 0:
        return TreeNode(postorder[post_right])

    # find root in postorder
    value = postorder[post_right]
    node = TreeNode(value)

    # find root in inorder
    in_left, in_right = inrange
    i = in_left
    while i <= in_right:
        if inorder[i] == value:
            break
        i += 1

    # generate left node
    left_inrange = (in_left, i - 1)
    left_diff = (i - 1) - in_left
    left_postrange = (post_left, post_left + left_diff)
    node.left = create_postorder_inorder(
        postorder, left_postrange, inorder, left_inrange
    )

    # generate right node
    right_inrange = (i + 1, in_right)
    right_diff = in_right - (i + 1)
    right_postrange = (post_right - right_diff - 1, post_right - 1)
    node.right = create_postorder_inorder(
        postorder, right_postrange, inorder, right_inrange
    )

    return node


# https://www.geeksforgeeks.org/construct-tree-from-given-inorder-and-preorder-traversal/
def create_preorder_inorder(preorder, prerange, inorder, inrange):
    pre_left, pre_right = prerange
    if pre_right - pre_left == 0:
        return TreeNode(preorder[pre_right])

    # find root in preorder
    value = preorder[pre_left]
    node = TreeNode(value)

    # find root in inorder
    in_left, in_right = inrange
    i = in_left
    while i <= in_right:
        if inorder[i] == value:
            break
        i += 1

    # get left node
    left_inorder = (in_left, i - 1)
    left_diff = (i - 1) - in_left
    left_preorder = (pre_left + 1, pre_left + left_diff + 1)
    node.left = create_preorder_inorder(preorder, left_preorder, inorder, left_inorder)

    # get right node
    right_inorder = (i + 1, in_right)
    right_diff = in_right - (i + 1)
    right_preorder = (pre_right - right_diff, pre_right)
    node.right = create_preorder_inorder(
        preorder, right_preorder, inorder, right_inorder
    )

    return node
