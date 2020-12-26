import pytest

from algorithms.string.anagram import check_anagram


@pytest.mark.string
@pytest.mark.parametrize("i", ["dog", "mom", "cinema"])
def test_check_anagram_good(i):
    assert check_anagram(i, i[::-1]) is True


@pytest.mark.string
def test_check_anagram_empty():
    assert check_anagram("", "") is True


@pytest.mark.string
@pytest.mark.parametrize("i", ["gag", ""])
def test_check_anagram_bad(i):
    assert check_anagram("gas", i) is False


@pytest.mark.string
@pytest.mark.parametrize("i1, i2", [("gas", "gass"), ("hat", "hats")])
def test_check_anagram_unequal(i1, i2):
    assert check_anagram(i1, i2) is False
