import pytest

from algorithms.sorting import merge_sort
from tests.helpers import is_sorted


@pytest.mark.array
@pytest.mark.sorting
def test_merge_sort(random_array):
    assert not is_sorted(random_array)
    merge_sort.sort(random_array)
    assert is_sorted(random_array)
