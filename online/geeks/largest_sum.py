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


largest_sum_non_adjacent([2, 4, 6, 2, 5]) == 13
largest_sum_non_adjacent([5, 1, 1, 5]) == 10
largest_sum_non_adjacent([]) == 0
largest_sum_non_adjacent([1]) == 1
largest_sum_non_adjacent([2, 1]) == 2
largest_sum_non_adjacent([3, 2, 5, 10, 7]) == 15
largest_sum_non_adjacent([3, 2, 7, 10]) == 13
