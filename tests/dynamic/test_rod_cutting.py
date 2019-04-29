import pytest

from algorithms.dynamic import rod_cutting as rods


@pytest.mark.dynamic
class TestRodCutting:
    @pytest.mark.parametrize("func", [rods.rod_cutting_dp, rods.rod_cutting_rec])
    def test_rod_cutting(self, func):
        prices = [1, 5, 8, 9, 10, 17, 17, 20, 24, 30]
        n = 4
        assert func(n, prices) == 10
        assert func(1, prices) == prices[0]
        assert func(0, prices) == 0

    def test_rod_cutting_equal(self):
        prices = [1, 5, 8, 9, 10, 17, 17, 20, 24, 30]
        for n in range(len(prices)):
            assert rods.rod_cutting_dp(n, prices) == rods.rod_cutting_rec(n, prices)
