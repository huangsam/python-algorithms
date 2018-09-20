# https://www.geeksforgeeks.org/count-possible-decodings-given-digit-sequence/
def count_decode(digit):
    n = len(digit)
    count = [0] * (n + 1)
    count[0] = 1
    count[1] = 1
    for i in range(2, n + 1):
        count[i] = 0
        if digit[i - 1] > '0':
            count[i] = count[i - 1]
        if digit[i - 2] == '1' or (digit[i - 2] == '2' and digit[i - 1] < '7'):
            count[i] += count[i - 2]
        i += 1
    return count[n]
