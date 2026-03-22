import pytest

from algorithms.string.regex_engine import regex_match


@pytest.mark.string
def test_regex_basic():
    assert regex_match("abc", "abc")
    assert not regex_match("abc", "abcd")
    assert not regex_match("abcd", "abc")


@pytest.mark.string
def test_regex_dot():
    assert regex_match("a.c", "abc")
    assert regex_match("...", "abc")
    assert not regex_match("..", "abc")


@pytest.mark.string
def test_regex_star():
    assert regex_match("a*", "")
    assert regex_match("a*", "aaa")
    assert regex_match("ab*c", "ac")
    assert regex_match("ab*c", "abbbc")
    assert regex_match(".*", "anything")


@pytest.mark.string
def test_regex_plus():
    assert not regex_match("a+", "")
    assert regex_match("a+", "a")
    assert regex_match("a+", "aaa")
    assert regex_match("ab+c", "abc")
    assert not regex_match("ab+c", "ac")


@pytest.mark.string
def test_regex_question():
    assert regex_match("a?", "")
    assert regex_match("a?", "a")
    assert not regex_match("a?", "aa")
    assert regex_match("ab?c", "abc")
    assert regex_match("ab?c", "ac")


@pytest.mark.string
def test_regex_complex():
    assert regex_match("a.*b?c+d", "axxxcd")
    assert regex_match("a.*b?c+d", "abcd")
    assert not regex_match("a.*b?c+d", "abd")
