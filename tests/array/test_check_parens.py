import pytest

from algorithms.array.check_parens import check_parens


@pytest.mark.string
@pytest.mark.stack
@pytest.mark.parametrize(
    "exp, valid",
    [
        ("[()]{}{[()()]()}", True),
        ("[(])", False),
        ("[{(})]", False),
        ("{()}", True),
    ],
)
def test_check_parens(exp, valid):
    assert check_parens(exp) is valid
