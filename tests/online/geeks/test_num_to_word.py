import pytest

import algorithms.online.geeks.num_to_word as word


@pytest.mark.string
class TestNumToWords:
    def test_num_to_word_single(self):
        assert word.num_to_word(0) == "zero"
        assert word.num_to_word(1) == "one"
        assert word.num_to_word(9) == "nine"

    def test_num_to_word_double(self):
        assert word.num_to_word(10) == "ten"
        assert word.num_to_word(11) == "eleven"
        assert word.num_to_word(19) == "nineteen"

    def test_num_to_word_hundred(self):
        assert word.num_to_word(100) == "one hundred"
        assert word.num_to_word(200) == "two hundred"
        assert word.num_to_word(202) == "two hundred two"
        assert word.num_to_word(999) == "nine hundred ninety nine"

    def test_num_to_word_thousands(self):
        assert word.num_to_word(1234) == "one thousand two hundred thirty four"
        assert word.num_to_word(10000001) == "ten million one"
        assert word.num_to_word(12000034) == "twelve million thirty four"
        assert word.num_to_word(10 ** 9 + 1) == "one billion one"
        assert word.num_to_word(10 ** 12 + 1) == "one trillion one"
