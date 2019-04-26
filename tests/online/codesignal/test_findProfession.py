import pytest

from algorithms.online.codesignal.findProfession import findProfession


@pytest.mark.tree
class TestFindProfession:
    @pytest.mark.parametrize(
        "level, pos, expected",
        [
            (3, 3, "Doctor"),
            (4, 2, "Doctor"),
            (1, 1, "Engineer"),
            (8, 100, "Engineer"),
            (25, 16777216, "Engineer"),
        ],
    )
    def test_escape(self, level, pos, expected):
        assert findProfession(level, pos) == expected
