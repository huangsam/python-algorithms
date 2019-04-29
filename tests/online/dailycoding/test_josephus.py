import pytest

from algorithms.online.dailycoding.josephus import josephus


@pytest.mark.dynamic
class TestJosephus:
    def test_josephus_survivor(self):
        for k in range(1, 200):
            assert josephus(1, k) == 1

    def test_josephus_2(self):
        for i in range(1, 2 ** 4 + 1):
            result = josephus(i, 2)
            if i & (i - 1) == 0:
                assert result == 1
            assert result % 2 == 1

    @pytest.mark.parametrize("n, k, expected", [(5, 3, 4), (5, 5, 2)])
    def test_josephus_k(self, n, k, expected):
        assert josephus(n, k) == expected
