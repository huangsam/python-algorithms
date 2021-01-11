def naive(content: str, pattern: str):
    p_len = len(pattern)
    c_len = len(content)
    if p_len == 0:
        return -1
    if c_len < p_len:
        return -1
    for ix in range(p_len, len(content) + 1):
        if content[ix - p_len : ix] == pattern:
            return ix - p_len
    return -1


# TODO: Complete this algorithm
# https://www.geeksforgeeks.org/kmp-algorithm-for-pattern-searching/
def kmp(content: str, pattern: str):
    pass
