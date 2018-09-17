import pytest

from online.glassdoor.check_paren import check_paren


class TestCheckParenthesis(object):

    @pytest.mark.parametrize('exp, valid', [
        ('[()]{}{[()()]()}', True),
        ('[(])', False),
        ('[{(})]', False),
        ('{()}', True),
    ])
    def test_check_paren(self, exp, valid):
        assert check_paren(exp) is valid
