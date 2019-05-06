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


# https://algorithms.tutorialhorizon.com//dynamic-programming-edit-distance-problem/
def edit_dist_dp(s1, s2):
    l1, l2 = len(s1), len(s2)
    dist = [[0] * (l2 + 1) for _ in range(l1 + 1)]
    for i in range(l2 + 1):
        dist[0][i] = i
    for i in range(l1 + 1):
        dist[i][0] = i
    for i in range(1, l1 + 1):
        for j in range(1, l2 + 1):
            if s1[i - 1] == s2[j - 1]:
                dist[i][j] = dist[i - 1][j - 1]
            else:
                dist[i][j] = 1 + min(dist[i - 1][j], dist[i][j - 1], dist[i - 1][j - 1])
    return dist[-1][-1]
