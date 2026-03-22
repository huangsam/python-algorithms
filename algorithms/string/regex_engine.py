def regex_match(pattern: str, text: str) -> bool:
    """A minimal backtracking regex engine supporting . * + and ?."""
    if not pattern:
        return not text

    first_match = bool(text) and pattern[0] in {text[0], "."}

    if len(pattern) >= 2 and pattern[1] in {"*", "+", "?"}:
        quantifier = pattern[1]
        remaining_pattern = pattern[2:]

        if quantifier == "*":
            # 0 matches (skip) OR 1+ matches (consume and stay)
            return regex_match(remaining_pattern, text) or (first_match and regex_match(pattern, text[1:]))
        elif quantifier == "+":
            # Must have at least one match, then acts like *
            return first_match and regex_match(pattern[0] + "*" + remaining_pattern, text[1:])
        elif quantifier == "?":
            # 0 matches (skip) OR 1 match (consume and move on)
            return regex_match(remaining_pattern, text) or (first_match and regex_match(remaining_pattern, text[1:]))

    return first_match and regex_match(pattern[1:], text[1:])
