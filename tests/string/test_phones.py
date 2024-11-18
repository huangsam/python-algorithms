import pytest

from algorithms.string.phones import get_phone_words_rec, get_phone_words_stk


@pytest.mark.math
@pytest.mark.string
@pytest.mark.parametrize("i", ["23456789", "3257", "3"])
def test_get_phone_words_rec_good(i: str):
    res = get_phone_words_rec(i)
    assert isinstance(res, list)
    assert len(res) == 3 ** len(i)


@pytest.mark.math
@pytest.mark.string
@pytest.mark.parametrize("i", ["23456789", "3257", "3"])
def test_get_phone_words_stk_good(i: str):
    res = get_phone_words_stk(i)
    assert isinstance(res, list)
    assert len(res) == 3 ** len(i)


@pytest.mark.math
@pytest.mark.string
def test_get_phone_words_rec_err():
    with pytest.raises(ValueError):
        get_phone_words_rec("")


@pytest.mark.math
@pytest.mark.string
def test_get_phone_words_stk_err():
    with pytest.raises(ValueError):
        get_phone_words_stk("")
