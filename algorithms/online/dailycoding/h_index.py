def h_index(papers):
    max_score = min(len(papers), max(papers))
    while max_score >= 0:
        valid = 0
        for paper in papers:
            if paper >= max_score:
                valid += 1
        if valid >= max_score:
            return max_score
        max_score -= 1
