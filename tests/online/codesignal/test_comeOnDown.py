import pytest

from algorithms.online.codesignal.comeOnDown import comeOnDown


@pytest.mark.online
def test_comeOnDown():
    assert comeOnDown(10, [2, 7]) == 3
    assert comeOnDown(5, [1, 2, 4]) == 3
