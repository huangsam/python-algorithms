import pytest

from algorithms.math.count_decode import count_decode


@pytest.mark.string
@pytest.mark.parametrize("digits, expected", [("111", 3), ("1234", 3), ("11", 2), ("1", 1), ("", 1)])
def test_count_decode(digits: str, expected: int):
    assert count_decode(digits) == expected
