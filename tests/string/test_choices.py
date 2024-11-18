from itertools import combinations as thecombo
from itertools import permutations as theperm

import pytest

from algorithms.string.choices import combinations as mycombo
from algorithms.string.choices import permutations as myperm


@pytest.fixture(params=["abcde", "fairy", "dinner", "eevee"])
def content(request) -> str:
    return request.param


@pytest.mark.math
@pytest.mark.string
def test_permutations(content: str):
    for rcur in range(1, len(content) + 1):
        tvalue = ["".join(v) for v in sorted(theperm(content, r=rcur))]
        mvalue = [v for v in myperm(content, r=rcur)]
        assert len(tvalue) == len(mvalue)
        assert tvalue == mvalue


@pytest.mark.math
@pytest.mark.string
def test_combinations(content: str):
    for rcur in range(1, len(content) + 1):
        tvalue = ["".join(v) for v in sorted(thecombo(content, r=rcur))]
        mvalue = [v for v in mycombo(content, r=rcur)]
        assert len(tvalue) == len(mvalue)
        assert tvalue == mvalue
