import pytest

from algorithms.online.cake.cake_thief import max_duffel_bag_value


@pytest.mark.dynamic
class TestCakeThief:
    def test_max_duffel_bag_value(self):
        cake_tuples = [(7, 160), (3, 90), (2, 15)]
        capacity = 20
        assert 555 == max_duffel_bag_value(cake_tuples, capacity)
