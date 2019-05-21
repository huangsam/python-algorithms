import pytest

from algorithms.online.dailycoding import chainable


@pytest.mark.string
class TestCanChain:
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
        ],
    )
    def test_can_chain(self, i, o):
        assert chainable.can_chain(i) == o
