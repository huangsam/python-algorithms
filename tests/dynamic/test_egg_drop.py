import pytest

from algorithms.dynamic.egg_drop import egg_drop, egg_drop_optimal


@pytest.mark.math
@pytest.mark.dynamic
def test_egg_drop():
    assert egg_drop(2, 10) == 4


@pytest.mark.math
@pytest.mark.dynamic
@pytest.mark.parametrize("eggs, floors, expected", [(2, 10, 4), (2, 36, 8)])
def test_egg_drop_optimal(eggs, floors, expected):
    assert egg_drop_optimal(eggs, floors) == expected
