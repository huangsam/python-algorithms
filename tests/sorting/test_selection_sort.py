import pytest

from sorting import selection_sort
from tests.utils import is_sorted


@pytest.mark.array
@pytest.mark.sorting
class TestSelectionSort:
    def test_selection_sort(self, array):
        assert not is_sorted(array)
        selection_sort.sort(array)
        assert is_sorted(array)
