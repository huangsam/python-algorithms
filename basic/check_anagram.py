def check_anagram(s1: str, s2: str) -> bool:
    """Determine if 2 Strings are anagrams.

    Args:
        s1: First string to evaluate.
        s2: Second string to evaluate.

    Returns:
        bool: True if applicable, False otherwise.
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


def main():
    assert check_anagram("dog", "god") is True
    assert check_anagram("mom", "mom") is True
    assert check_anagram("cinema", "iceman") is True
    assert check_anagram("gas", "gag") is False
    assert check_anagram("gas", "gass") is False


if __name__ == '__main__':
    main()
