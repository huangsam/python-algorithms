import pytest

from algorithms.array.common_elements import common_elements


@pytest.mark.array
@pytest.mark.parametrize(
    "a1, a2, a3, expected",
    [
        ([], [], [], []),
        ([1, 1, 1, 3], [1, 3], [1, 1], [1]),
        ([1, 3, 5, 7, 9], [1, 5, 9], [3, 5, 7, 9], [5, 9]),
        ([1, 3, 5], [1, 3, 5], [1, 3, 5, 9], [1, 3, 5]),
    ],
)
def test_common_elements(a1: list, a2: list, a3: list, expected: list):
    result = common_elements(a1, a2, a3)
    for i, j in zip(result, expected):
        assert i == j
