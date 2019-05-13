def is_valid(papers, target):
    valid = 0
    for paper in papers:
        if paper >= target:
            valid += 1
    return valid >= target


def h_index(papers):
    papers.sort()
    start = min(len(papers), max(papers))
    end = 0
    result = 0
    while start >= end:
        mid = (start + end) // 2
        if is_valid(papers, mid):
            result = max(result, mid)
            # valid -> look upwards for higher valid
            end = mid + 1
        else:
            # invalid -> look downwards for a good valid
            start = mid - 1
    return result
