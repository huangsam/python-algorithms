def naive(content, pattern):
    plen = len(pattern)
    clen = len(content)
    if plen == 0:
        return -1
    if clen < plen:
        return -1
    for ix in range(plen, len(content) + 1):
        if content[ix - plen : ix] == pattern:
            return ix - plen
    return -1


# https://www.geeksforgeeks.org/kmp-algorithm-for-pattern-searching/
def kmp(content, pattern):
    pass
