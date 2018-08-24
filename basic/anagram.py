def check_anagram(s1, s2):
    """Determine if 2 Strings are anagrams.

    Args:
        s1: First string to evaluate.
        s2: Second string to evaluate.

    Returns:
        True if applicable, False otherwise.
    """
    smap = {}
    for c1 in s1:
        if c1 in smap:
            smap[c1] += 1
        else:
            smap[c1] = 1
    for c2 in s2:
        if c2 not in smap:
            return False
        smap[c2] -= 1
        if smap[c2] < 0:
            return False
    return True
