def permutations(content, r=None):
    rval = r or len(content)
    result = permutations_wh(content, r=rval)
    return [p for p in sorted(result)]


def permutations_wh(content, r):
    if r == 0:
        return []
    if r == 1:
        return [ch for ch in content]
    result = []
    for ix, head in enumerate(content):
        remainder = content[:ix] + content[ix + 1 :]
        for rseq in permutations_wh(remainder, r - 1):
            result.append(head + rseq)
    return result


def combinations(content, r=None):
    rval = r or len(content)
    result = combinations_wh(content, r=rval)
    return [c for c in sorted(result)]


def combinations_wh(content, r):
    if r == 0:
        return []
    if r == 1:
        return [ch for ch in content]
    result = []
    for ix, head in enumerate(content):
        tail = content[ix + 1 :]
        for tseq in combinations_wh(tail, r - 1):
            result.append(head + tseq)
    return result
