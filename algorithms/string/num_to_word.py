from collections import deque

_ANSWERS = {
    0: "zero",
    1: "one",
    2: "two",
    3: "three",
    4: "four",
    5: "five",
    6: "six",
    7: "seven",
    8: "eight",
    9: "nine",
    10: "ten",
    11: "eleven",
    12: "twelve",
    13: "thirteen",
    14: "fourteen",
    15: "fifteen",
    16: "sixteen",
    17: "seventeen",
    18: "eighteen",
    19: "nineteen",
    20: "twenty",
    30: "thirty",
    40: "forty",
    50: "fifty",
    60: "sixty",
    70: "seventy",
    80: "eighty",
    90: "ninety",
}

_THOUSANDS = ["thousand", "million", "billion"]


# https://www.geeksforgeeks.org/convert-number-to-words/
def num_to_word(n):
    # Handle bad inputs
    if n <= -1:
        raise ValueError("integer cannot be negative")
    elif n >= 1000000000000:
        raise ValueError("integer is too big")

    # Handle a single digit group
    if n < 20:
        return _ANSWERS[n]
    elif n < 100:
        prefix = _ANSWERS[n // 10 * 10]
        if n % 10 == 0:
            return prefix
        else:
            return f"{prefix} {num_to_word(n % 10)}"
    elif n < 1000:
        prefix = _ANSWERS[n // 100]
        if n % 100 == 0:
            return f"{prefix} hundred"
        else:
            return f"{prefix} hundred {num_to_word(n % 100)}"

    word_list = deque()

    # Handle first digit group
    if n % 1000 > 0:
        word_list.appendleft(num_to_word(n % 1000))

    # Handle remaining digit groups
    n_head = n // 1000
    i = 0
    while n_head > 0:
        if i > len(_THOUSANDS) - 1:
            raise ValueError("too big for function to process")
        if n_head % 1000 > 0:
            word_list.appendleft(f"{num_to_word(n_head % 1000)} {_THOUSANDS[i]}")
        n_head //= 1000
        i += 1

    return " ".join(word_list)
