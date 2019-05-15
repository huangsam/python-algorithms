# https://algorithms.tutorialhorizon.com//the-word-break-problem/
def split_word(seq, book, cache):
    if seq in cache:
        return cache[seq]
    for i in range(1, len(seq)):
        lseq, rseq = seq[:i], seq[i:]
        if lseq not in book:
            continue
        if rseq in book or split_word(rseq, book, cache):
            cache[seq] = True
            return cache[seq]
    return False
