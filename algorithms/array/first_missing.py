def first_missing(arr: list[int]):
    mapping = {1: False}

    # Assume val + 1 is False if unset
    for val in arr:
        if val <= 0:
            continue
        mapping[val] = True
        mapping.setdefault(val + 1, False)

    minimum = None
    maximum = 0

    # Identify min-max values
    for key, val in mapping.items():
        if val is False:
            if minimum is None or minimum > key:
                minimum = key
        if maximum < key:
            maximum = key

    return minimum if minimum else maximum + 1


# https://www.geeksforgeeks.org/find-the-smallest-positive-number-missing-from-an-unsorted-array/
def first_missing_optimal(arr: list[int]):
    # Ignore zeros and negatives
    for i, val in enumerate(arr):
        if val < 0:
            arr[i] = 0
    maximum = 0

    # Idempotent negative
    for i, val in enumerate(arr):
        a_val = abs(val)
        if maximum < a_val:
            maximum = a_val
        if 1 <= a_val <= len(arr):
            if arr[a_val - 1] > 0:
                arr[a_val - 1] *= -1

    # Identify first positive
    minimum = None
    for i, val in enumerate(arr):
        if val > 0:
            minimum = i + 1
            break

    return minimum if minimum else maximum + 1
