import pytest

from algorithms.sorting.merge_in_place import merge_in_place
from tests.helpers import is_sorted


@pytest.mark.array
@pytest.mark.sorting
def test_merge_in_place_a():
    a = [1, 2]
    b = []
    merge_in_place(a, b)
    assert is_sorted(a)


@pytest.mark.array
@pytest.mark.sorting
def test_merge_in_place_b():
    a = [None, None]
    b = [1, 2]
    merge_in_place(a, b)
    assert is_sorted(a)


@pytest.mark.array
@pytest.mark.sorting
def test_merge_in_place_unique():
    a = [1, 2, 3, None, None, None]
    b = [4, 5, 6]
    merge_in_place(a, b)
    assert is_sorted(a)


@pytest.mark.array
@pytest.mark.sorting
def test_merge_in_place_zigzag():
    a = [1, 3, 5, None, None, None]
    b = [2, 4, 6]
    merge_in_place(a, b)
    assert is_sorted(a)


@pytest.mark.array
@pytest.mark.sorting
def test_merge_in_place_big():
    a = [1, 3, 5, 8, 10, 14, None, None, None, None, None]
    b = [2, 4, 6, 9, 11]
    merge_in_place(a, b)
    assert is_sorted(a)
