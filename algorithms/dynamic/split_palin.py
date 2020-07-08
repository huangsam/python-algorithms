from typing import Dict

from algorithms.constants import MAX_INT


def is_palin(seq: str):
    return seq[::-1] == seq


# https://algorithms.tutorialhorizon.com/dynamic-programming-split-the-string-into-minimum-number-of-palindromes/
def split_palin(seq: str, cache: Dict[str, int]):
    if seq in cache:
        return cache[seq]
    if is_palin(seq):
        cache[seq] = 0
        return cache[seq]
    result = MAX_INT
    for i in range(1, len(seq)):
        lseq, rseq = seq[:i], seq[i:]
        lval, rval = split_palin(lseq, cache), split_palin(rseq, cache)
        result = min(result, 1 + lval + rval)
    cache[seq] = result
    return result
