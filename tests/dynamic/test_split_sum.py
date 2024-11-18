import pytest

from algorithms.dynamic.split_sum import split_sum


@pytest.mark.array
def test_split_sum_one():
    assert split_sum([1, 2, 3, 4], 1) == 10


@pytest.mark.array
def test_split_sum_two():
    assert split_sum([1, 2, 3, 4], 2) == 6


@pytest.mark.array
def test_split_sum_three():
    assert split_sum([1, 2, 3, 4], 3) == 4


@pytest.mark.array
def test_split_sum_all():
    assert split_sum([1, 2, 3, 4], 4) == 4


@pytest.mark.array
def test_split_sum_sample():
    assert split_sum([5, 1, 2, 7, 3, 4], 3) == 8


@pytest.mark.array
def test_split_sum_painter_three():
    assert split_sum([1] * 6, 3) == 2


@pytest.mark.array
def test_split_sum_painter_five():
    assert split_sum([1] * 9, 5) == 2


@pytest.mark.array
def test_split_sum_painter_equal():
    assert split_sum([1] * 12, 12) == 1
