# https://www.geeksforgeeks.org/convert-number-to-words/
def num_to_word(n):
    single = [
        "zero",
        "one",
        "two",
        "three",
        "four",
        "five",
        "six",
        "seven",
        "eight",
        "nine",
    ]
    double = [
        "ten",
        "eleven",
        "twelve",
        "thirteen",
        "fourteen",
        "fifteen",
        "sixteen",
        "seventeen",
        "eighteen",
        "nineteen",
    ]
    tens = [
        "",
        "",
        "twenty",
        "thirty",
        "forty",
        "fifty",
        "sixty",
        "seventy",
        "eighty",
        "ninety",
    ]
    if n < 0:
        raise ValueError("must be a positive integer")
    if n < 10:
        return single[n]
    if n < 20:
        return double[n % 10]
    if n < 10 ** 2:
        return tens[n // 10] + " " + num_to_word(n % 10)
    if n < 10 ** 3:
        prefix = single[n // 100]
        if n % 100 == 0:
            return prefix + " hundred"
        else:
            return prefix + " hundred " + num_to_word(n % 100)
    thousands = ["thousand", "million", "billion", "trillion"]
    for i in range(len(thousands)):
        divisor = 1000 ** (i + 1)
        bound = 1000 ** (i + 2)
        print(n, bound, divisor, "cutting")
        if n < bound:
            return (
                num_to_word(n // divisor)
                + " "
                + thousands[i]
                + " "
                + num_to_word(n % divisor)
            )
    raise ValueError("too big for function to process")
