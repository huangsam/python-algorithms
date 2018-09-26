import pytest

from online.geeks.autocomplete import autocomplete


class TestAutocomplete(object):

    @pytest.mark.parametrize("s, queries, expected", [
        ('de', ['dog', 'deer', 'deal'], ['deer', 'deal']),
        ('ab', ['abc', 'abcd', 'aa', 'abbbaba'], ['abc', 'abcd', 'abbbaba']),
    ])
    def test_autocomplete(self, s, queries, expected):
        result = autocomplete(s, queries)
        assert set(result) == set(expected)
