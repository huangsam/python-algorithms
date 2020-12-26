import pytest

from algorithms.math.josephus import josephus


@pytest.mark.math
@pytest.mark.dynamic
def test_josephus_survivor():
    for k in range(1, 200):
        assert josephus(1, k) == 1


@pytest.mark.math
@pytest.mark.dynamic
def test_josephus_2():
    for i in range(1, 2 ** 4 + 1):
        result = josephus(i, 2)
        if i & (i - 1) == 0:
            assert result == 1
        assert result % 2 == 1


@pytest.mark.math
@pytest.mark.dynamic
@pytest.mark.parametrize("n, k, expected", [(5, 3, 4), (5, 5, 2)])
def test_josephus_k(n, k, expected):
    assert josephus(n, k) == expected
