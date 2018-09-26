# https://www.geeksforgeeks.org/find-the-longest-substring-with-k-unique-characters-in-a-given-string/
def longest_k_distinct(s, k, answers):
    if len(s) == 0:
        return ''
    if s in answers:
        return answers[s]
    if is_valid(s, k) is True:
        answers[s] = s
    else:
        left_longest = longest_k_distinct(s[1:], k, answers)
        right_longest = longest_k_distinct(s[:-1], k, answers)
        answers[s] = longest_two(left_longest, right_longest)
    return answers[s]


def is_valid(s, k):
    unique = set(list(s))
    return len(unique) == k


def longest_two(s1, s2):
    return s1 if len(s1) > len(s2) else s2
