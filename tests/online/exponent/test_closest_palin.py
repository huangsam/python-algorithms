from algorithms.online.exponent.closest_palin import closest_palin


class TestClosestPalin:
    def test_single_digit_zero(self):
        assert closest_palin("0") == "1"

    def test_single_digit_one(self):
        assert closest_palin("1") == "0"

    def test_single_digit_five(self):
        assert closest_palin("5") == "4"

    def test_two_digits_ten(self):
        assert closest_palin("10") == "9"

    def test_two_digits_ninety_nine(self):
        assert closest_palin("99") == "101"

    def test_three_digits_one_hundred(self):
        assert closest_palin("100") == "99"

    def test_three_digits_one_twenty_three(self):
        assert closest_palin("123") == "121"

    def test_three_digits_nine_nine_nine(self):
        assert closest_palin("999") == "1001"

    def test_four_digits_one_thousand(self):
        assert closest_palin("1000") == "999"

    def test_one_through_five(self):
        assert closest_palin("12345") == "12321"
