import pytest

from online.youtube.largest_rect import largest_rect


@pytest.mark.array
class TestLargestRect(object):
    @pytest.mark.parametrize(
        "histo, expected",
        [
            ([1, 3, 5, 3, 0, 2, 6, 6, 1, 0, 3, 6], 12),
            ([1, 3, 5, 3, 2, 2, 3, 3, 1, 0, 3, 6], 14),
            ([1, 3, 2, 1, 2], 5),
        ],
    )
    def test_largest_rect(self, histo, expected):
        assert largest_rect(histo) == expected
