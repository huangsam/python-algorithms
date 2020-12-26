import pytest

from algorithms.online.dailycoding import chainable


@pytest.mark.string
@pytest.mark.parametrize(
    "i, o",
    [
        (["chair", "height", "racket", "touch", "tunic"], True),
        (["chair", "racket", "tunic"], True),
        (["am", "ma", "mam", "ama"], True),
        (["tulip", "pat"], True),
        (["chair", "racket"], False),
        (["chair", "racket", "touch"], False),
        (["chair", "racket", "touch", "hairy"], False),
        (["geek", "king"], True),
        (["for", "geek", "rig", "kaf"], True),
        (["aab", "bac", "aaa", "cda"], True),
        (["aaa", "bbb", "baa", "aab"], True),
        (["aaa"], True),
        (["aaa", "bbb"], False),
        (["abc", "efg", "cde", "ghi", "ija"], True),
        (["ijk", "kji", "abc", "cba"], False),
    ],
)
def test_can_chain(i, o):
    assert chainable.can_chain(i) == o
