import pytest

from algorithms.dynamic.knapsack import knapsack_dp


@pytest.mark.dynamic
class TestKnapsack:
    def test_knapsack_dp(self):
        weight = 50
        items = [(10, 60), (20, 100), (30, 120)]
        result = knapsack_dp(weight, items)
        assert result == 220
