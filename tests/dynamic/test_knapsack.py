import pytest

from algorithms.dynamic.knapsack import knapsack_binary_dp, knapsack_binary_rec, knapsack_infinite


@pytest.mark.dynamic
@pytest.mark.parametrize(
    "w, i, o",
    [
        (10, [], 0),
        (10, [(10, 20)], 20),
        (20, [(10, 20)], 20),
        (20, [(7, 160), (3, 90), (2, 15)], 265),
        (50, [(10, 60), (20, 100), (30, 120)], 220),
    ],
)
@pytest.mark.parametrize("f", [knapsack_binary_dp, knapsack_binary_rec])
def test_knapsack_binary(f, w: int, i: list[int], o: int):
    assert f(w, i) == o


@pytest.mark.dynamic
@pytest.mark.parametrize(
    "w, i, o",
    [
        (20, [(10, 100), (5, 50), (2, 20)], 200),
        (20, [(7, 160), (3, 90), (2, 15)], 555),
    ],
)
def test_knapsack_inf(w: int, i: list[tuple[int, int]], o: int):
    assert knapsack_infinite(w, i) == o
