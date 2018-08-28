from basic.anagram import check_anagram


class TestAnagram(object):

    def test_check_anagram_good(self):
        assert check_anagram('dog', 'god') is True
        assert check_anagram('mom', 'mom') is True
        assert check_anagram('cinema', 'iceman') is True

    def test_check_anagram_bad(self):
        assert check_anagram('gas', 'gag') is False
        assert check_anagram('gas', 'gass') is False
