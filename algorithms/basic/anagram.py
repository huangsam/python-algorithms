from typing import Dict


def check_anagram(s1: str, s2: str):
    if len(s1) != len(s2):
        return False
    cmap: Dict[str, int] = {}
    for c1 in s1:
        if c1 in cmap:
            cmap[c1] += 1
        else:
            cmap[c1] = 1
    for c2 in s2:
        if c2 not in cmap:
            return False
        cmap[c2] -= 1
        if cmap[c2] < 0:
            return False
    return True
