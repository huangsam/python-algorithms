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
        "friend",
        "have",
        "I",
        "is",
        "Jain",
        "my",
        "Sumit",
        "this",
    }

    @pytest.mark.parametrize(
        "i, o",
        [
            ("IamSumit", "I am Sumit"),
            ("facebook", "face book"),
            ("thisdogiscool", "this dog is cool"),
            ("Ihavemydog", "I have my dog"),
            ("mycoolfriendisJain", "my cool friend is Jain"),
            ("thisfacebookfriendIhave", "this face book friend I have"),
        ],
    )
    def test_split_word_good(self, i, o):
        result = word.split_word(i, self.book, cache={})
        assert result == o

    @pytest.mark.parametrize("i", ["thisisadog", "myspace", "face", "book"])
    def test_split_word_bad(self, i):
        result = word.split_word(i, self.book, cache={})
        assert result == word.NOT_FOUND
