# https://www.geeksforgeeks.org/maximum-sum-such-that-no-two-elements-are-adjacent/
def largest_sum_non_adjacent(arr):
    if len(arr) < 3:
        return 0 if len(arr) == 0 else max(arr)
    result = None
    answers = [0] * len(arr)
    answers[0] = arr[0]
    answers[1] = arr[1]
    for i in range(2, len(arr)):
        cur_max = arr[i]
        for j in range(i - 2, -1, -1):
            cur_val = arr[i] + answers[j]
            cur_max = max(cur_max, cur_val)
        answers[i] = cur_max
        if result is None or result < cur_max:
            result = cur_max
    return result


# https://www.geeksforgeeks.org/largest-sum-contiguous-subarray/
def largest_sum_adjacent(arr):
    if len(arr) == 0:
        return 0
    answers = [0] * len(arr)
    result = answers[0] = max(arr[0], 0)
    for i in range(1, len(arr)):
        val = answers[i - 1] + arr[i]
        answers[i] = max(val, 0)
        if result is None or answers[i] > result:
            result = answers[i]
    return result
