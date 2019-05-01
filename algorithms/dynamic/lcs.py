def lcs_rec(astr, bstr):
    return lcs_wh(astr, 0, bstr, 0)


def lcs_wh(astr, aind, bstr, bind):
    if aind >= len(astr):
        return 0
    if bind >= len(bstr):
        return 0
    result = 0
    while bind < len(bstr):
        if astr[aind] == bstr[bind]:
            alternate = 1 + lcs_wh(astr, aind + 1, bstr, bind + 1)
            result = max(result, alternate)
        bind += 1
    return result
