import pytest

import algorithms.online.dailycoding.h_index as hind


@pytest.mark.array
class TestHIndex:
    @pytest.mark.parametrize(
        "i, o",
        [
            ([4, 3, 0, 1, 5], 3),
            ([0, 1, 3, 4, 5], 3),
            ([0, 1, 6, 9, 11, 15, 16, 19], 6),
            ([0, 0, 0, 0, 0], 0),
            ([1, 1, 1, 1, 1], 1),
        ],
    )
    def test_h_index_sample(self, i, o):
        assert hind.h_index(i) == o

    def test_h_index_same(self):
        for i in range(1, 10):
            papers = [i for _ in range(i)]
            assert hind.h_index(papers) == i
