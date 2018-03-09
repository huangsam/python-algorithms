def base_encode(num, base=62):
    digits = []
    while num > 0:
        remainder = num % base
        digits.append(remainder)
        num = num / base
    return reversed(digits)


encoding = base_encode(1234567)
result = ''.join(map(str, encoding))
print(result)
