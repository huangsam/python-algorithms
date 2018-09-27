import pytest

from online.geeks.egg_drop import (
    egg_drop,
    egg_drop_optimal,
)


class TestEggDrop(object):

    @pytest.mark.parametrize('eggs, floors, expected', [
        (2, 10, 4),
        (2, 36, 8),
    ])
    @pytest.mark.parametrize('func', [egg_drop, egg_drop_optimal])
    def test_egg_drop(self, eggs, floors, expected, func):
        assert func(eggs, floors) == expected
