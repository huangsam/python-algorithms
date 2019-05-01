def lcs_rec(astr, bstr):
    return lcs_wh(astr, 0, bstr, 0)


def lcs_wh(astr, aind, bstr, bind):
    if aind == len(astr) or bind == len(bstr):
        return 0

    if astr[aind] == bstr[bind]:
        match = 1 + lcs_wh(astr, aind + 1, bstr, bind + 1)
        return match

    alcs = lcs_wh(astr, aind + 1, bstr, bind)
    blcs = lcs_wh(astr, aind, bstr, bind + 1)
    return max(alcs, blcs)


# https://algorithms.tutorialhorizon.com//dynamic-programming-longest-common-subsequence/
def lcs_dp(astr, bstr):
    alen, blen = len(astr), len(bstr)
    matches = [[0] * alen for _ in blen]
    return matches[-1][-1]
