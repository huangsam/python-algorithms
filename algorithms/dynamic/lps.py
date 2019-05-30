# https://www.geeksforgeeks.org/longest-palindromic-subsequence-dp-12/
def lps_dp(seq):
    n = len(seq)
    length = [[0 for x in range(n)] for x in range(n)]

    for i in range(n):
        length[i][i] = 1

    for cl in range(2, n + 1):
        for i in range(n - cl + 1):
            j = i + cl - 1
            if seq[i] == seq[j] and cl == 2:
                length[i][j] = 2
            elif seq[i] == seq[j]:
                length[i][j] = length[i + 1][j - 1] + 2
            else:
                length[i][j] = max(length[i][j - 1], length[i + 1][j])

    return length[0][n - 1]
