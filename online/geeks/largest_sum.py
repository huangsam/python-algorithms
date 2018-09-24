# https://www.geeksforgeeks.org/maximum-sum-such-that-no-two-elements-are-adjacent/
def largest_sum_non_adjacent(arr):
    if len(arr) == 0:
        return 0
    elif len(arr) < 3:
        return max(arr)
    answers = [0] * len(arr)
    answers[0] = arr[0]
    answers[1] = arr[1]
    for i in range(2, len(arr)):
        cur_max = None
        cur_val = arr[i]
        j = i - 2
        while j >= 0:
            if cur_max is None or cur_max < answers[j]:
                cur_max = answers[j]
            j -= 1
        answers[i] = cur_max + cur_val
    return answers[len(arr) - 1]
