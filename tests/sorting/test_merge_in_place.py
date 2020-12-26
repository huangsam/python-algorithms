import pytest

from algorithms.sorting import merge_in_place as mip
from tests.helpers import is_sorted


@pytest.mark.array
@pytest.mark.sorting
def test_merge_in_place_a():
    a = [1, 2]
    b = []
    mip.merge_in_place(a, b)
    assert is_sorted(a)


@pytest.mark.array
@pytest.mark.sorting
def test_merge_in_place_b():
    a = [None, None]
    b = [1, 2]
    mip.merge_in_place(a, b)
    assert is_sorted(a)


@pytest.mark.array
@pytest.mark.sorting
def test_merge_in_place_unique():
    a = [1, 2, 3, None, None, None]
    b = [4, 5, 6]
    mip.merge_in_place(a, b)
    assert is_sorted(a)


@pytest.mark.array
@pytest.mark.sorting
def test_merge_in_place_zigzag():
    a = [1, 3, 5, None, None, None]
    b = [2, 4, 6]
    mip.merge_in_place(a, b)
    assert is_sorted(a)


@pytest.mark.array
@pytest.mark.sorting
def test_merge_in_place_big():
    a = [1, 3, 5, 8, 10, 14, None, None, None, None, None]
    b = [2, 4, 6, 9, 11]
    mip.merge_in_place(a, b)
    assert is_sorted(a)
