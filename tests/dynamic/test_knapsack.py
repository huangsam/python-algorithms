import pytest

from algorithms.dynamic import knapsack as knap


@pytest.mark.dynamic
class TestKnapsack:
    @pytest.mark.parametrize(
        "w, i, o",
        [
            (10, [], 0),
            (10, [(10, 20)], 20),
            (20, [(10, 20)], 20),
            (20, [(7, 160), (3, 90), (2, 15)], 265),
            (50, [(10, 60), (20, 100), (30, 120)], 220),
        ],
    )
    @pytest.mark.parametrize("f", [knap.knapsack_dp, knap.knapsack_rec])
    def test_knapsack_dp(self, f, w, i, o):
        weight = 50
        assert f(w, i) == o

    def test_knapsack_inf_1(self):
        weight = 20
        items = [(7, 160), (3, 90), (2, 15)]
        result = knap.knapsack_inf(weight, items)
        assert result == 555

    def test_knapsack_inf_2(self):
        weight = 20
        items = [(10, 100), (5, 50), (2, 20)]
        result = knap.knapsack_inf(weight, items)
        assert result == 200
