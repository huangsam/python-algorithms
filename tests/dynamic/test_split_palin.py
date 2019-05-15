import pytest

import algorithms.dynamic.split_palin as palin


@pytest.mark.string
@pytest.mark.dynamic
class TestSplitPalin:
    @pytest.mark.parametrize(
        "i, o",
        [
            ("", 0),
            ("aba", 0),
            ("abaa", 1),
            ("ababbbbb", 1),
            ("xabaay", 3),
            ("abcde", 4),
        ],
    )
    def test_split_palin_empty(self, i, o):
        cache = {}
        result = palin.split_palin(i, cache)
        assert result == o
