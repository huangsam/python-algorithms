import pytest

from algorithms.math.power_set import power_set


@pytest.mark.math
@pytest.mark.parametrize("size", [0, 1, 2, 3, 5, 8])
def test_power_set(size: int):
    vals = tuple([val for val in range(size)])
    result = list(power_set(vals))
    assert len(result) == 2**size
