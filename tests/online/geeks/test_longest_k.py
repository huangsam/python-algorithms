import pytest

from online.geeks.longest_k import longest_k_distinct


class TestLongestK(object):

    @pytest.mark.parametrize("given, k, expected", [
        ('abcba', 2, 'bcb'),
        ('ddcbaaa', 3, 'cbaaa'),
        ('ddcbaaa', 2, 'baaa'),
        ('a', 2, ''),
    ])
    def test_longest_k_distinct(self, given, k, expected):
        assert longest_k_distinct(given, k) == expected
