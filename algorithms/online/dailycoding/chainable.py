def can_chain(words):
    """Determine whether words can be chained to form a circle."""
    fmap = {}
    for word in words:
        ch = word[0]
        if ch not in fmap:
            fmap[ch] = set()
        fmap[ch].add(word)
    return can_chain_wh(words[0], words, fmap, set())


def can_chain_wh(cur_word, words, fmap, seen):
    if len(words) == len(seen):
        return True
    if cur_word in seen:
        return False
    seen.add(cur_word)
    lch = cur_word[-1]
    if lch not in fmap:
        return False
    for next_word in fmap[lch]:
        if can_chain_wh(next_word, words, fmap, seen):
            return True
    return False
