import pytest

from algorithms.array.merge_k import merge_k_heap, merge_k_split, merge_two_arrays


@pytest.mark.array
@pytest.mark.parametrize(
    "arrays, expected",
    [
        (
            [[10, 15, 30], [12, 15, 20], [17, 20, 32]],
            [10, 12, 15, 15, 17, 20, 20, 30, 32],
        ),
        ([], []),
        ([[], [], []], []),
        ([[], [1], [1, 2]], [1, 1, 2]),
        ([[1]], [1]),
        ([[1], [1, 3, 5], [1, 10, 20, 30, 40]], [1, 1, 1, 3, 5, 10, 20, 30, 40]),
    ],
)
@pytest.mark.parametrize("func", [merge_k_split, merge_k_heap])
def test_merge_k(arrays: list[list[int]], expected: list[int], func):
    result = func(arrays)
    for i, j in zip(result, expected):
        assert i == j


@pytest.mark.parametrize(
    "arr1, arr2, expected",
    [
        ([10, 15, 30], [12, 15, 20], [10, 12, 15, 15, 20, 30]),
        ([], [], []),
        ([1], [], [1]),
        ([1, 2, 3], [1, 5], [1, 1, 2, 3, 5]),
    ],
)
def test_merge_two_arrays(arr1, arr2, expected):
    result = merge_two_arrays(arr1, arr2)
    for i, j in zip(result, expected):
        assert i == j
