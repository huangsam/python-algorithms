import pytest

from algorithms.tree.creation import create_postorder_inorder, create_preorder_inorder
from algorithms.tree.inorder import inorder_recursive


@pytest.mark.tree
def test_create_postorder_inorder():
    postorder = [6, 7, 5, 3, 4, 2, 1]
    postrange = (0, len(postorder) - 1)
    inorder = [6, 5, 7, 1, 3, 2, 4]
    inrange = (0, len(inorder) - 1)
    root = create_postorder_inorder(postorder, postrange, inorder, inrange)
    assert root is not None and root.value == 1
    assert inorder_recursive(root) == inorder


@pytest.mark.tree
def test_create_preorder_inorder():
    preorder = [1, 5, 6, 7, 2, 3, 4]
    prerange = (0, len(preorder) - 1)
    inorder = [6, 5, 7, 1, 3, 2, 4]
    inrange = (0, len(inorder) - 1)
    root = create_preorder_inorder(preorder, prerange, inorder, inrange)
    assert root is not None and root.value == 1
    assert inorder_recursive(root) == inorder
