import pytest

from algorithms.dynamic.rod_cutting import rod_cutting_dp, rod_cutting_rec


@pytest.mark.dynamic
@pytest.mark.parametrize("func", [rod_cutting_dp, rod_cutting_rec])
def test_rod_cutting(func):
    prices = [1, 5, 8, 9, 10, 17, 17, 20, 24, 30]
    n = 4
    assert func(n, prices) == 10
    assert func(1, prices) == prices[0]
    assert func(0, prices) == 0


@pytest.mark.dynamic
def test_rod_cutting_equal():
    prices = [1, 5, 8, 9, 10, 17, 17, 20, 24, 30]
    for n in range(len(prices)):
        assert rod_cutting_dp(n, prices) == rod_cutting_rec(n, prices)
