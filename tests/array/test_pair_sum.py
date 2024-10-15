import pytest

from algorithms.array.pair_sum import pair_sum


@pytest.fixture(scope="function")
def sum_array() -> list[int]:
    return [3, 7, 10, 9, 1, 5]


@pytest.mark.math
@pytest.mark.array
def test_pair_sum_multiple(sum_array: list[int]):
    target = 10
    result = pair_sum(sum_array, target)
    assert len(result) == 2
    assert (5, 5) not in result
    assert (7, 3) in result
    assert (1, 9) in result


@pytest.mark.math
@pytest.mark.array
def test_pair_sum_single(sum_array: list[int]):
    target = 15
    result = pair_sum(sum_array, target)
    assert len(result) == 1
    assert (5, 10) in result


@pytest.mark.math
@pytest.mark.array
def test_pair_sum_none(sum_array: list[int]):
    target = 2
    result = pair_sum(sum_array, target)
    assert len(result) == 0
