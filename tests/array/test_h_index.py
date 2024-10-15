import pytest

from algorithms.array import h_index as hind


@pytest.mark.array
@pytest.mark.parametrize(
    "i, o",
    [
        ([4, 3, 0, 1, 5], 3),
        ([0, 1, 3, 4, 5], 3),
        ([0, 1, 6, 9, 11, 15, 16, 19], 6),
        ([0, 9, 10, 20, 30, 40, 50, 60, 80], 8),
        ([0, 0, 0, 0, 0], 0),
        ([1, 1, 1, 1, 1], 1),
    ],
)
def test_h_index_sample(i: list[int], o: int):
    assert hind.h_index(i) == o


@pytest.mark.array
@pytest.mark.parametrize("i", [_ for _ in range(1, 13)])
def test_h_index_same(i: int):
    papers = [i for _ in range(i)]
    assert hind.h_index(papers) == i
