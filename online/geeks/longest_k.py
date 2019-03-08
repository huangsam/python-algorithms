def longest_k_distinct(s, k):
    if len(s) == 0:
        return ""
    if is_valid(s, k) is True:
        return s
    left = longest_k_distinct(s[1:], k)
    right = longest_k_distinct(s[:-1], k)
    return left if len(left) > len(right) else right


def is_valid(s, k):
    unique = set(list(s))
    return len(unique) == k


# https://www.geeksforgeeks.org/find-the-longest-substring-with-k-unique-characters-in-a-given-string/
def longest_k_distinct_optimal(s, k):
    counts = {}
    unique = 0
    for val in s:
        if val not in counts:
            counts[val] = 0
            unique += 1
        counts[val] += 1
    if unique < k:
        return ""
    counts = {}
    start, end = 0, 0
    result_start = 0
    result_size = 0
    for val in s:
        if val not in counts:
            counts[val] = 0
        counts[val] += 1
        end += 1
        while is_valid_optimal(counts, k) is False:
            sval = s[start]
            counts[sval] -= 1
            if counts[sval] == 0:
                del counts[sval]
            start += 1
        if (end - start) > result_size:
            result_size = end - start
            result_start = start
    return s[result_start : (result_start + result_size)]


def is_valid_optimal(counts, k):
    return len(counts) <= k
