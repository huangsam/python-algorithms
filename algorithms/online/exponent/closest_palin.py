def closest_palin(s: str) -> str:
    """Find the closest palindrome of a given number.

    A reasonable approach is to look at the midpoint of the number and
    generate prefixes based on prefix, prefix+1 and prefix-1. Then
    mirror those prefixes to form palindromes and choose the closest one.
    For edge cases, we also consider 10..01 and 9..9.
    """
    n = len(s)
    if n == 1:
        return str(int(s) - 1) if s != "0" else "1"

    prefix = int(s[: (n + 1) // 2])
    candidates = []

    # Generate palindromes from prefix-1, prefix, prefix+1
    for i in [-1, 0, 1]:
        new_prefix = str(prefix + i)
        if n % 2 == 0:
            palin = new_prefix + new_prefix[::-1]
        else:
            palin = new_prefix + new_prefix[-2::-1]
        candidates.append(palin)

    # Edge cases
    candidates.append("9" * (n - 1))  # e.g., 1000 -> 999
    candidates.append("1" + ("0" * (n - 1)) + "1")  # e.g., 999 -> 1001

    original_num = int(s)

    # Filter out the original number itself
    valid_candidates = [c for c in candidates if c != s]

    # Find the closest palindrome
    closest = min(valid_candidates, key=lambda cand: (abs(int(cand) - original_num), int(cand)))

    return closest
