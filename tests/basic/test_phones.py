import pytest

from algorithms.basic import phones


@pytest.mark.math
@pytest.mark.string
class TestPhoneWords:
    def test_get_phone_words_rec_all(self):
        res = phones.get_phone_words_rec("23456789")
        assert isinstance(res, list)
        assert len(res) == 3 ** 8

    def test_get_phone_words_stk_all(self):
        res = phones.get_phone_words_stk("23456789")
        assert isinstance(res, list)
        assert len(res) == 3 ** 8

    def test_get_phone_words_rec_one(self):
        res = phones.get_phone_words_rec("2")
        assert isinstance(res, list)
        assert len(res) == 3

    def test_get_phone_words_stk_one(self):
        res = phones.get_phone_words_stk("2")
        assert isinstance(res, list)
        assert len(res) == 3

    def test_get_phone_words_rec_err(self):
        with pytest.raises(ValueError):
            phones.get_phone_words_rec("")

    def test_get_phone_words_stk_err(self):
        with pytest.raises(ValueError):
            phones.get_phone_words_stk("")
