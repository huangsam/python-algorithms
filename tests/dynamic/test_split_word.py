import pytest

import algorithms.dynamic.split_word as word


@pytest.mark.string
@pytest.mark.dynamic
class TestSplitWord:
    book = {
        "am",
        "book",
        "cool",
        "dog",
        "face",
        "facebook",
        "have",
        "I",
        "is",
        "Jain",
        "Sumit",
        "this",
    }

    @pytest.mark.parametrize("i", ["IamSumit", "facebook", "thisdogiscool"])
    def test_split_word_good(self, i):
        cache = {}
        result = word.split_word(i, self.book, cache)
        assert result is True

    @pytest.mark.parametrize("i", ["thisisadog", "face", "book"])
    def test_split_word_bad(self, i):
        cache = {}
        result = word.split_word(i, self.book, cache)
        assert result is False
