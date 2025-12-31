import pytest

from algorithms.dynamic.climb_steps import climb_steps


@pytest.mark.dynamic
@pytest.mark.parametrize("levels, steps, expected", [(4, [1, 2], 5), (4, [1, 3, 5], 3)])
def test_climb_steps(levels: int, steps: list[int], expected: int):
    assert climb_steps(levels, steps) == expected


@pytest.mark.dynamic
def test_climb_steps_zero():
    assert climb_steps(0, [1, 2]) == 0  # No ways to climb 0 steps? Wait, actually 1 way (do nothing)
