import pytest

from algorithms.online.geeks.first_missing import first_missing, first_missing_optimal


@pytest.mark.array
class TestFirstMissing:
    @pytest.mark.parametrize(
        "arr, missing",
        [
            ([3, 4, -1, 1], 2),
            ([1, 2, 0], 3),
            ([1, 2, 1, 1, 1], 3),
            ([-1, -3, -5, -7], 1),
            ([0, 0], 1),
            ([1, 1, 2, 2, 3, 3], 4),
            ([1, 2, 3, 4], 5),
            ([2, 3, 7, 6, 8, -1, -10, 15], 1),
            ([2, 3, -7, 6, 8, 1, -10, 15], 4),
            ([1, 1, 0, -1, -2], 2),
            ([3, 5], 1),
        ],
    )
    @pytest.mark.parametrize("func", [first_missing, first_missing_optimal])
    def test_first_missing(self, arr, missing, func):
        assert func(arr) is missing
