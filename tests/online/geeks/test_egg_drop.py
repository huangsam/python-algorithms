import pytest

from algorithms.online.geeks.egg_drop import egg_drop, egg_drop_optimal


@pytest.mark.dynamic
class TestEggDrop:
    def test_egg_drop(self):
        assert egg_drop(2, 10) == 4

    @pytest.mark.parametrize("eggs, floors, expected", [(2, 10, 4), (2, 36, 8)])
    def test_egg_drop_optimal(self, eggs, floors, expected):
        assert egg_drop_optimal(eggs, floors) == expected
