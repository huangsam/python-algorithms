import pytest

from algorithms.online.geeks.climb_steps import climb_steps


@pytest.mark.dynamic
@pytest.mark.parametrize("levels, steps, expected", [(4, (1, 2), 5), (4, (1, 3, 5), 3)])
def test_climb_steps(levels, steps, expected):
    assert climb_steps(levels, steps) == expected
