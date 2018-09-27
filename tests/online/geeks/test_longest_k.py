import pytest

from online.geeks.longest_k import (
    longest_k_distinct,
    longest_k_distinct_optimal,
)


class TestLongestK(object):

    @pytest.mark.parametrize('kin, kval, expected', [
        ('a', 2, ''),
        ('aabbcc', 1, 'aa'),
        ('aabbcc', 2, 'aabb'),
        ('aabbcc', 3, 'aabbcc'),
        ('hatsofftowhoever', 4, 'tsoffto'),
    ])
    def test_longest_k_distinct(self, kin, kval, expected):
        assert longest_k_distinct(kin, kval, {}) == expected

    @pytest.mark.parametrize('kin, kval, expected', [
        ('a', 2, ''),
        ('aabbcc', 1, 'aa'),
        ('aabbcc', 2, 'aabb'),
        ('aabbcc', 3, 'aabbcc'),
        ('hatsofftowhoever', 4, 'tsoffto'),
    ])
    def test_longest_k_distinct_optimal(self, kin, kval, expected):
        assert longest_k_distinct_optimal(kin, kval) == expected
