def is_valid(papers, target):
    start, end = 0, len(papers) - 1
    result = end
    while start <= end:
        mid = (start + end) // 2
        val = papers[mid]
        if val >= target:
            result = min(result, mid)
            # valid -> look down for smaller val
            end = mid - 1
        else:
            # invalid -> look up for valid val
            start = mid + 1
    return (len(papers) - result) >= target


def h_index(papers):
    papers.sort()
    start = min(len(papers), max(papers))
    end = 0
    result = 0
    while start >= end:
        mid = (start + end) // 2
        if is_valid(papers, mid):
            result = max(result, mid)
            # valid -> look up for higher h
            end = mid + 1
        else:
            # invalid -> look down for valid h
            start = mid - 1
    return result
