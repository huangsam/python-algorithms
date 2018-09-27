import pytest

from online.geeks.climb_steps import climb_steps


class TestClimbSteps(object):

    @pytest.mark.parametrize('levels, steps, expected', [
        (4, (1, 2), 5),
        (4, (1, 3, 5), 3),
    ])
    def test_climb_steps(self, levels, steps, expected):
        assert climb_steps(levels, steps) == expected
