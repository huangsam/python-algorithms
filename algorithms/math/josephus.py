import math


# https://en.wikipedia.org/wiki/Josephus_problem
# https://www.youtube.com/watch?v=7Ezs8UtNK9s
# https://www.youtube.com/watch?v=VH9Yvy9pb84
def josephus(n, q):
    d = 1
    while d <= (q - 1) * n:
        d = math.ceil(q * d / (q - 1))
    return q * n + 1 - d
