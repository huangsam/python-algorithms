def swap_new(s1, a, b):
    sa = s1[a]
    sb = s1[b]
    return s1[:a] + sb + s1[(a + 1) : b] + sa + s1[(b + 1) :]


# https://www.geeksforgeeks.org/linkedin-interview-experience-6/
def swap_chars(s1, s2):
    if len(s1) != len(s2):
        return False
    i = 0
    while i < len(s1):
        while i < len(s1) and s1[i] == s2[i]:
            i += 1
        if i + 2 < len(s1):
            if s1[i + 2] != s2[i]:
                return False
            s1 = swap_new(s1, i, i + 2)
        i += 1
    return s1 == s2
