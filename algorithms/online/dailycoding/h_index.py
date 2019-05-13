def h_index(papers):
    max_score = max(papers)
    while max_score > 0:
        valid = 0
        for paper in papers:
            if paper >= max_score:
                valid += 1
        if valid >= max_score:
            return max_score
        max_score -= 1
    return 0
