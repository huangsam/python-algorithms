import pytest

from algorithms.dynamic import knapsack as knap


@pytest.mark.dynamic
class TestKnapsack:
    def test_knapsack_dp_1(self):
        weight = 50
        items = [(10, 60), (20, 100), (30, 120)]
        result = knap.knapsack_dp(weight, items)
        assert result == 220

    def test_knapsack_dp_2(self):
        weight = 20
        items = [(7, 160), (3, 90), (2, 15)]
        result = knap.knapsack_dp(weight, items)
        assert result == 265

    def test_knapsack_rec_1(self):
        weight = 50
        items = [(10, 60), (20, 100), (30, 120)]
        result = knap.knapsack_rec(weight, items)
        assert result == 220

    def test_knapsack_rec_2(self):
        weight = 20
        items = [(7, 160), (3, 90), (2, 15)]
        result = knap.knapsack_rec(weight, items)
        assert result == 265

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
