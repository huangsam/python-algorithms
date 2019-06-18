def naive(content, pattern):
    plen = len(pattern)
    for ix in range(plen, len(content)):
        if content[ix - plen : ix] == pattern:
            return True
    return False


# https://www.geeksforgeeks.org/kmp-algorithm-for-pattern-searching/
def kmp(content, pattern):
    pass
