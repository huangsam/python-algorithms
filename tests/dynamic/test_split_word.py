import pytest

from algorithms.dynamic.split_word import NOT_FOUND, split_word

_BOOK: set[str] = {
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


@pytest.mark.string
@pytest.mark.dynamic
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
def test_split_word_good(i: str, o: str):
    result = split_word(i, _BOOK, cache={})
    assert result == o


@pytest.mark.string
@pytest.mark.dynamic
@pytest.mark.parametrize("i", ["thisisadog", "myspace", "face", "book"])
def test_split_word_bad(i: str):
    result = split_word(i, _BOOK, cache={})
    assert result == NOT_FOUND
