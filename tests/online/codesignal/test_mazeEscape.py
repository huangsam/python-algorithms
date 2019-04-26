import pytest

from algorithms.online.codesignal.mazeEscape import mazeEscape


@pytest.mark.graph
class TestMazeEscape:
    @pytest.mark.parametrize(
        "w, h, dist, impassable",
        [
            (4, 4, 6, [1, 0, 1, 1, 2, 2, 3, 1]),
            (
                10,
                10,
                58,
                [
                    0,
                    1,
                    0,
                    5,
                    1,
                    1,
                    1,
                    3,
                    1,
                    5,
                    1,
                    7,
                    1,
                    8,
                    2,
                    1,
                    2,
                    3,
                    2,
                    5,
                    2,
                    7,
                    3,
                    1,
                    3,
                    3,
                    3,
                    5,
                    3,
                    7,
                    3,
                    9,
                    4,
                    1,
                    4,
                    3,
                    4,
                    5,
                    4,
                    7,
                    5,
                    1,
                    5,
                    3,
                    5,
                    5,
                    5,
                    7,
                    5,
                    8,
                    6,
                    1,
                    6,
                    3,
                    6,
                    5,
                    6,
                    7,
                    7,
                    1,
                    7,
                    3,
                    7,
                    5,
                    7,
                    7,
                    7,
                    9,
                    8,
                    1,
                    8,
                    3,
                    8,
                    5,
                    8,
                    7,
                    9,
                    3,
                    9,
                    7,
                    9,
                    8,
                ],
            ),
            (
                15,
                4,
                17,
                [
                    1,
                    0,
                    8,
                    0,
                    1,
                    1,
                    6,
                    1,
                    10,
                    1,
                    12,
                    1,
                    13,
                    1,
                    1,
                    2,
                    2,
                    2,
                    3,
                    2,
                    4,
                    2,
                    6,
                    2,
                    8,
                    2,
                    9,
                    2,
                    10,
                    2,
                    12,
                    2,
                ],
            ),
            (
                15,
                15,
                28,
                [
                    0,
                    1,
                    0,
                    3,
                    1,
                    3,
                    1,
                    6,
                    1,
                    7,
                    1,
                    8,
                    1,
                    9,
                    1,
                    10,
                    1,
                    11,
                    1,
                    12,
                    1,
                    13,
                    2,
                    0,
                    2,
                    1,
                    2,
                    3,
                    2,
                    4,
                    2,
                    6,
                    3,
                    3,
                    3,
                    6,
                    3,
                    8,
                    3,
                    9,
                    3,
                    10,
                    3,
                    11,
                    3,
                    12,
                    3,
                    13,
                    3,
                    14,
                    4,
                    1,
                    4,
                    3,
                    4,
                    5,
                    4,
                    6,
                    5,
                    1,
                    5,
                    3,
                    5,
                    6,
                    5,
                    7,
                    5,
                    8,
                    5,
                    9,
                    5,
                    10,
                    5,
                    11,
                    5,
                    12,
                    5,
                    13,
                    6,
                    1,
                    7,
                    1,
                    7,
                    3,
                    7,
                    5,
                    7,
                    7,
                    7,
                    8,
                    7,
                    10,
                    7,
                    11,
                    7,
                    12,
                    7,
                    13,
                    7,
                    14,
                    8,
                    1,
                    8,
                    3,
                    8,
                    5,
                    8,
                    7,
                    9,
                    1,
                    9,
                    3,
                    9,
                    5,
                    9,
                    7,
                    10,
                    1,
                    10,
                    3,
                    10,
                    5,
                    10,
                    7,
                    11,
                    1,
                    11,
                    3,
                    11,
                    5,
                    11,
                    7,
                    12,
                    1,
                    12,
                    3,
                    12,
                    5,
                    12,
                    7,
                    13,
                    1,
                    13,
                    3,
                    13,
                    5,
                    13,
                    7,
                    13,
                    8,
                    13,
                    9,
                    13,
                    10,
                    13,
                    11,
                    13,
                    12,
                    13,
                    13,
                    14,
                    5,
                ],
            ),
        ],
    )
    def test_escape(self, w, h, dist, impassable):
        assert mazeEscape(w, h, impassable) == dist
