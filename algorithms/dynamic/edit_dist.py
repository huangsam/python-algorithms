def edit_dist_rec(s1, s2):
    return edit_dist_wh(s1, len(s1), s2, len(s2))


def edit_dist_wh(s1, i1, s2, i2):
    if i1 == 0:
        return i2
    if i2 == 0:
        return i1
    if s1[i1 - 1] == s2[i2 - 1]:
        return edit_dist_wh(s1, i1 - 1, s2, i2 - 1)
    return min(
        1 + edit_dist_wh(s1, i1 - 1, s2, i2),
        1 + edit_dist_wh(s1, i1, s2, i2 - 1),
        1 + edit_dist_wh(s1, i1 - 1, s2, i2 - 1),
    )


def edit_dist_dp(s1, s2):
    dist = [[0] * len(s2) for _ in range(len(s1))]
    for i in range(len(s1)):
        for j in range(len(s2)):
            if s1[i - 1] == s2[j - 1]:
                dist[i][j] = dist[i - 1][j - 1]
            else:
                dist[i][j] = min(
                    1 + dist[i - 1][j], 1 + dist[i][j - 1], 1 + dist[i - 1][j - 1]
                )
    return dist[-1][-1]
