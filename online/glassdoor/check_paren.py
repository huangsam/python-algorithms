def check_paren(exp):
    mapping = {
        ')': '(',
        '}': '{',
        ']': '[',
    }
    seen = []
    for ch in exp:
        if ch in mapping.values():
            seen.append(ch)
        elif seen and mapping.get(ch) == seen[-1]:
            seen.pop()
    return len(seen) == 0
