import pytest

from algorithms.basic.anagram import check_anagram


@pytest.mark.string
class TestAnagram:
    @pytest.mark.parametrize("i", ["dog", "mom", "cinema"])
    def test_check_anagram_good(self, i):
        assert check_anagram(i, i[::-1]) is True

    def test_check_anagram_empty(self):
        assert check_anagram("", "") is True

    @pytest.mark.parametrize("i", ["gag", ""])
    def test_check_anagram_bad(self, i):
        assert check_anagram("gas", i) is False

    @pytest.mark.parametrize("i1, i2", [("gas", "gass"), ("hat", "hats")])
    def test_check_anagram_unequal(self, i1, i2):
        assert check_anagram(i1, i2) is False
