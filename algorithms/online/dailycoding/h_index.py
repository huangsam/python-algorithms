def is_valid(papers, target):
    valid = 0
    for paper in papers:
        if paper >= target:
            valid += 1
    return valid >= target


def h_index(papers):
    max_score = min(len(papers), max(papers))
    while max_score >= 0:
        if is_valid(papers, max_score):
            return max_score
        max_score -= 1
