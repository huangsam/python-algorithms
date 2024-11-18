import pytest

from algorithms.dynamic.climb_steps import climb_steps


@pytest.mark.dynamic
@pytest.mark.parametrize("levels, steps, expected", [(4, [1, 2], 5), (4, [1, 3, 5], 3)])
def test_climb_steps(levels: int, steps: list[int], expected: int):
    assert climb_steps(levels, steps) == expected
