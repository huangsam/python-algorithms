def can_chain(words):
    first_map = {}
    for word in words:
        ch = word[0]
        if ch not in first_map:
            first_map[ch] = set()
        first_map[ch].add(word)
    return can_chain_wh(words[0], words, first_map, set())


# https://www.geeksforgeeks.org/given-array-strings-find-strings-can-chained-form-circle/
# https://www.geeksforgeeks.org/find-array-strings-can-chained-form-circle-set-2/
def can_chain_wh(cur_word, words, first_map, seen):
    if len(words) == len(seen):
        return True
    if cur_word in seen:
        return False
    seen.add(cur_word)
    lch = cur_word[-1]
    if lch not in first_map:
        return False
    for next_word in first_map[lch]:
        if can_chain_wh(next_word, words, first_map, seen):
            return True
    return False
