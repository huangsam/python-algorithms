import pytest

import algorithms.basic.word_search as wsearch


@pytest.mark.string
class TestNaive:
    @pytest.mark.parametrize(
        "astr, bstr, ix",
        [
            ("hello", "", -1),
            ("ab", "abc", -1),
            ("hello", "helli", -1),
            ("hello", "hello", 0),
            ("hello world i am trying", "i am", 12),
            ("hello world", "world", 6),
        ],
    )
    def test_naive(self, astr, bstr, ix):
        assert wsearch.naive(astr, bstr) == ix
