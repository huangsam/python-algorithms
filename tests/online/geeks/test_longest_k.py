import pytest

from online.geeks.longest_k import (
    longest_k_distinct,
    longest_k_distinct_optimal,
)


@pytest.mark.string
class TestLongestK(object):

    @pytest.mark.parametrize('kin, kval, expected', [
        ('a', 2, ''),
        ('aabbcc', 1, 'aa'),
        ('aabbcc', 2, 'aabb'),
        ('aabbcc', 3, 'aabbcc'),
        ('hatsofftowhoever', 4, 'tsoffto'),
    ])
    @pytest.mark.parametrize('func', [longest_k_distinct, longest_k_distinct_optimal])
    def test_longest_k_distinct(self, kin, kval, expected, func):
        assert func(kin, kval) == expected
