# https://www.geeksforgeeks.org/merging-intervals/
def merge_intervals(intervals: list[list[int]]) -> list[list[int]]:
    intervals.sort()
    return _merge_intervals_work(intervals)


def _merge_intervals_work(intervals: list[list[int]]) -> list[list[int]]:
    if len(intervals) < 2:
        return intervals
    if len(intervals) == 2:
        return _merge_two(intervals[0], intervals[1])

    middle = len(intervals) // 2
    left = _merge_intervals_work(intervals[:middle])
    right = _merge_intervals_work(intervals[middle:])

    result = left[:-1] + _merge_two(left[-1], right[0]) + right[1:]
    return result


def _merge_two(i1: list[int], i2: list[int]) -> list[list[int]]:
    i1_min, i1_max = i1
    i2_min, i2_max = i2
    if i1_max < i2_min:
        return [i1, i2]
    return [[min(i1_min, i2_min), max(i1_max, i2_max)]]
