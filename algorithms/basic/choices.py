def permutations(content, r=None):
    rval = r or len(content)
    cresult = permutations_wh(content, r=rval)
    return [v for v in sorted(cresult)]


def permutations_wh(content, r):
    if r == 0:
        return []
    if r == 1:
        return [ch for ch in content]
    result = []
    for ix in range(len(content)):
        hchar = content[ix]
        ncontent = content[:ix] + content[ix + 1 :]
        nresult = permutations_wh(ncontent, r - 1)
        for nseq in nresult:
            result.append(hchar + nseq)
    return result


def combinations(content, r=None):
    rval = r or len(content)
    cresult = combinations_wh(content, r=rval)
    return [v for v in sorted(cresult)]


def combinations_wh(content, r):
    if r == 0:
        return []
    if r == 1:
        return [ch for ch in content]
    result = []
    for ix in range(len(content)):
        hchar = content[ix]
        tcontent = content[ix + 1 :]
        tresult = combinations_wh(tcontent, r - 1)
        for tseq in tresult:
            result.append(hchar + tseq)
    return result
