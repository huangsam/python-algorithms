from typing import Optional


def permutations(content: str, r: Optional[int] = None):
    rval = r or len(content)
    result = _permutations_wh(content, r=rval)
    return [p for p in sorted(result)]


def _permutations_wh(content: str, r: int):
    if r == 0:
        return []
    if r == 1:
        return [ch for ch in content]
    result = []
    for ix, head in enumerate(content):
        remainder = content[:ix] + content[ix + 1 :]
        for rseq in _permutations_wh(remainder, r - 1):
            result.append(head + rseq)
    return result


def combinations(content: str, r: Optional[int] = None):
    rval = r or len(content)
    result = _combinations_wh(content, r=rval)
    return [c for c in sorted(result)]


def _combinations_wh(content: str, r: int):
    if r == 0:
        return []
    if r == 1:
        return [ch for ch in content]
    result = []
    for ix, head in enumerate(content):
        tail = content[ix + 1 :]
        for tseq in _combinations_wh(tail, r - 1):
            result.append(head + tseq)
    return result
