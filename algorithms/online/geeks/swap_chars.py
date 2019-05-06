def swap_new(s1, a, b):
    sa = s1[a]
    sb = s1[b]
    return s1[:a] + sb + s1[(a + 1) : b] + sa + s1[(b + 1) :]


def swap_chars(s1, s2):
    if len(s1) != len(s2):
        return False
    if s1 == s2:
        return True
    i = 0
    while i < len(s1) and s1[i] == s2[i]:
        i += 1
    if i + 2 < len(s1):
        if s1[i + 2] == s2[i]:
            s1_new = swap_new(s1, i, i + 2)
            return swap_chars(s1_new[1:], s2[1:])
    return False
