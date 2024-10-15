import pytest

from algorithms.array.depth_sum import depth_sum, depth_sum_stack


@pytest.mark.array
@pytest.mark.stack
@pytest.mark.parametrize(
    "nested, expected",
    [([[1, 1], 2, [1, 1]], 10), ([[[3], [1, 2]]], 18), ([1, [2], [[3]]], 14)],
)
@pytest.mark.parametrize("func", [depth_sum, depth_sum_stack])
def test_depth_sum(func, nested: list, expected: int):
    assert func(nested) == expected
