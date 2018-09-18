import pytest

from online.glassdoor.depth_sum import (
    depth_sum,
    depth_sum_stack,
)


class TestDepthSum(object):

    @pytest.mark.parametrize('nested, expected', [
        ([[1, 1], 2, [1, 1]], 10),
        ([[[3], [1, 2]]], 18),
        ([1, [2], [[3]]], 14),
    ])
    @pytest.mark.parametrize('func', [depth_sum, depth_sum_stack])
    def test_depth_sum(self, nested, expected, func):
        assert func(nested) == expected
