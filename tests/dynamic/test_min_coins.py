import pytest

from algorithms.dynamic.min_coins import min_coins


@pytest.mark.dynamic
@pytest.mark.parametrize("amt, ans", [(75, 3), (10, 1), (4, 4), (0, 0)])
def test_min_coins(amt: int, ans: int):
    coins = [1, 5, 10, 25]
    assert min_coins(coins, amt) == ans
