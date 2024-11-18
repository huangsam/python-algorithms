import pytest

from algorithms.sorting import selection_sort
from tests.helpers import is_sorted


@pytest.mark.array
@pytest.mark.sorting
def test_selection_sort(random_array):
    assert not is_sorted(random_array)
    selection_sort.sort(random_array)
    assert is_sorted(random_array)
