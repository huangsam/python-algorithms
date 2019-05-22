import pytest

from algorithms.basic import phones


@pytest.mark.math
@pytest.mark.string
class TestPhoneWords:
    @pytest.mark.parametrize("i", ["23456789", "3257", "3"])
    def test_get_phone_words_rec(self, i):
        res = phones.get_phone_words_rec(i)
        assert isinstance(res, list)
        assert len(res) == 3 ** len(i)

    @pytest.mark.parametrize("i", ["23456789", "3257", "3"])
    def test_get_phone_words_stk(self, i):
        res = phones.get_phone_words_stk(i)
        assert isinstance(res, list)
        assert len(res) == 3 ** len(i)

    def test_get_phone_words_rec_err(self):
        with pytest.raises(ValueError):
            phones.get_phone_words_rec("")

    def test_get_phone_words_stk_err(self):
        with pytest.raises(ValueError):
            phones.get_phone_words_stk("")
