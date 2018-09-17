import pytest

from online.glassdoor.check_parens import check_parens


class TestCheckParenthesis(object):

    @pytest.mark.parametrize('exp, valid', [
        ('[()]{}{[()()]()}', True),
        ('[(])', False),
        ('[{(})]', False),
        ('{()}', True),
    ])
    def test_check_parens(self, exp, valid):
        assert check_parens(exp) is valid
