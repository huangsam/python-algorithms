import pytest

from algorithms.sorting import merge_sort
from tests.utils import is_sorted


@pytest.mark.array
@pytest.mark.sorting
def test_merge_sort(array):
    assert not is_sorted(array)
    merge_sort.sort(array)
    assert is_sorted(array)
