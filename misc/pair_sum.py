def pair_sum(arr, target):
    """Return pair of array values that yield target sum.

    Args:
        arr (list): Array of integer values.
        target (int): Target value that we're shooting for.

    Returns:
        dict: "Set" of pairs that were found.
    """
    ind_to_diff = {}
    pairs = {}
    for val in arr:
        if val in ind_to_diff:
            left, right = val, ind_to_diff[val]
            pairs[(left, right)] = True
        diff = target - val
        ind_to_diff[diff] = val
    return pairs


def main():
    target = 10
    array = [3, 7, 10, 9, 1, 5]
    result = pair_sum(array, target)
    assert len(result) == 2
    assert (5, 5) not in result
    assert (7, 3) in result
    assert (1, 9) in result

    target = 15
    result = pair_sum(array, target)
    assert len(result) == 1
    assert (5, 10) in result

    target = 2
    result = pair_sum(array, target)
    assert len(result) == 0


if __name__ == '__main__':
    main()
