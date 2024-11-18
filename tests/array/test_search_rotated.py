import pytest

from algorithms.array.search_rotated import search_min, search_one


def _cycle(n: int) -> list[list[int]]:
    arr: list[int] = [1 + 3 * i for i in range(n)]
    cycles: list[list[int]] = []
    for i in range(n):
        rev = arr[::-1]
        cycles.append(rev[:i][::-1] + rev[i:][::-1])
    return cycles


@pytest.mark.array
@pytest.mark.parametrize("any_cycle", _cycle(5))
def test_search_one(any_cycle):
    for val in any_cycle:
        assert search_one(any_cycle, val) is True


@pytest.mark.array
@pytest.mark.parametrize("any_cycle", _cycle(5))
def test_search_min(any_cycle):
    assert search_min(any_cycle) == min(any_cycle)


@pytest.mark.array
def test_search_min_dupe():
    dupe_cycle = [3, 3, 3, 5, 5, 7, 9, 9, 9, 1, 1, 2, 2, 2]
    assert search_min(dupe_cycle) == min(dupe_cycle)
