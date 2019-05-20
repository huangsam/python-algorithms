import pytest

import algorithms.online.geeks.num_to_word as word


@pytest.mark.math
@pytest.mark.string
class TestNumToWords:
    @pytest.mark.parametrize(
        "a, o",
        [
            (0, "zero"),
            (9, "nine"),
            (10, "ten"),
            (19, "nineteen"),
            (100, "one hundred"),
            (200, "two hundred"),
            (202, "two hundred two"),
            (999, "nine hundred ninety nine"),
            (1234, "one thousand two hundred thirty four"),
            (10101, "ten thousand one hundred one"),
            (101010, "one hundred one thousand ten"),
            (10000001, "ten million one"),
            (12000034, "twelve million thirty four"),
            (10 ** 9 + 1, "one billion one"),
            (10 ** 12 + 1, "one trillion one"),
        ],
    )
    def test_num_to_word_good(self, a, o):
        assert word.num_to_word(a) == o

    def test_num_to_word_negative(self):
        with pytest.raises(ValueError):
            word.num_to_word(-1)

    def test_num_to_word_overflow(self):
        with pytest.raises(ValueError):
            word.num_to_word(10 ** 20)
