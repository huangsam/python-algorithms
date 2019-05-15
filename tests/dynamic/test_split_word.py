import pytest

import algorithms.dynamic.split_word as word


@pytest.mark.string
@pytest.mark.dynamic
class TestSplitWord:
    book = {"I", "have", "Jain", "Sumit", "am", "this", "dog"}

    def test_split_word_good(self):
        cache = {}
        result = word.split_word("IamSumit", self.book, cache)
        assert result is True

    def test_split_word_bad(self):
        cache = {}
        result = word.split_word("thisisadog", self.book, cache)
        assert result is False
