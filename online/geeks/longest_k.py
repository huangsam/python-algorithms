# https://www.geeksforgeeks.org/find-the-longest-substring-with-k-unique-characters-in-a-given-string/
def longest_k_distinct(s, k, answers):
    if len(s) == 0:
        return ''
    if s in answers:
        return answers[s]
    if is_valid(s, k) is True:
        answers[s] = s
    else:
        answers[s] = longest_two(
            longest_k_distinct(s[1:], k, answers),
            longest_k_distinct(s[:-1], k, answers)
        )
    return answers[s]


def is_valid(s, k):
    unique = set(list(s))
    return len(unique) == k


def longest_two(s1, s2):
    return s1 if len(s1) > len(s2) else s2
