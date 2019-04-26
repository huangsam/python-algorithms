import pytest

from algorithms.online.geeks.check_parens import check_parens


@pytest.mark.string
@pytest.mark.stack
class TestCheckParenthesis:
    @pytest.mark.parametrize(
        "exp, valid",
        [
            ("[()]{}{[()()]()}", True),
            ("[(])", False),
            ("[{(})]", False),
            ("{()}", True),
        ],
    )
    def test_check_parens(self, exp, valid):
        assert check_parens(exp) is valid
