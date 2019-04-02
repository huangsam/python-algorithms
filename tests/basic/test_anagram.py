import pytest

from basic.anagram import check_anagram


@pytest.mark.string
class TestAnagram:
    def test_check_anagram_good(self):
        assert check_anagram("dog", "god") is True
        assert check_anagram("mom", "mom") is True
        assert check_anagram("cinema", "iceman") is True

    def test_check_anagram_empty(self):
        assert check_anagram("", "") is True

    def test_check_anagram_bad(self):
        assert check_anagram("gas", "gag") is False
        assert check_anagram("gas", "") is False

    def test_check_anagram_unequal(self):
        assert check_anagram("gas", "gass") is False
        assert check_anagram("hat", "hats") is False
