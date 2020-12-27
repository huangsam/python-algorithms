from typing import Dict, List


# https://www.youtube.com/watch?v=XKu_SEDAykw
def pair_sum(arr: List[int], target: int):
    """Return pair of array values that yield target sum.

    Args:
        arr (list): Array of integer values.
        target (int): Target value that we're shooting for.

    Returns:
        dict: "Set" of pairs that were found.
    """
    ind_to_diff: Dict[int, int] = {}
    pairs = {}
    for val in arr:
        if val in ind_to_diff:
            left, right = val, ind_to_diff[val]
            pairs[(left, right)] = True
        diff = target - val
        ind_to_diff[diff] = val
    return pairs
