import pytest

from algorithms.tree.levelorder import levelorder_basic, levelorder_height_with_node, levelorder_height_with_queues


@pytest.mark.tree
def test_levelorder_basic(simple_tree):
    result = levelorder_basic(simple_tree)
    assert result == [1, 2, 3, 4, 5, 6]


@pytest.mark.tree
@pytest.mark.parametrize("func", [levelorder_height_with_node, levelorder_height_with_queues])
def test_levelorder_height(simple_tree, func):
    result = list(func(simple_tree))
    values = [item.node.value for item in result]
    levels = [item.level for item in result]
    assert values == [1, 2, 3, 4, 5, 6]
    assert levels == [0, 1, 2, 2, 3, 3]
