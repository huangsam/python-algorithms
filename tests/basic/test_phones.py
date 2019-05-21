import pytest

from algorithms.basic import phones


@pytest.mark.math
@pytest.mark.string
class TestPhoneWords:
    def test_get_phone_words_rec(self):
        res = phones.get_phone_words_rec()
        assert isinstance(res, list)
        assert len(res) == 3 ** 8

    def test_get_phone_words_stk(self):
        res = phones.get_phone_words_stk()
        assert isinstance(res, list)
        assert len(res) == 3 ** 8
