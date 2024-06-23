NOT_FOUND = "N/A"


# https://algorithms.tutorialhorizon.com/the-word-break-problem/
def split_word(seq: str, book: str, cache: dict[str, str]):
    if seq in cache:
        return cache[seq]
    for i in range(1, len(seq)):
        lseq, rseq = seq[:i], seq[i:]
        if lseq not in book:
            continue
        if rseq in book:
            cache[seq] = lseq + " " + rseq
            return cache[seq]
        rsplit = split_word(rseq, book, cache)
        if rsplit != NOT_FOUND:
            cache[seq] = lseq + " " + rsplit
            return cache[seq]
    return NOT_FOUND
