import pytest

from algorithms.array.largest_rect import largest_rect


@pytest.mark.math
@pytest.mark.array
@pytest.mark.parametrize(
    "histo, expected",
    [
        ([1, 3, 5, 3, 0, 2, 6, 6, 1, 0, 3, 6], 12),
        ([1, 3, 5, 3, 2, 2, 3, 3, 1, 0, 3, 6], 14),
        ([1, 3, 2, 1, 2], 5),
    ],
)
def test_largest_rect(histo: list[int], expected: int):
    assert largest_rect(histo) == expected
