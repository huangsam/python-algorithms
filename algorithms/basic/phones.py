def get_phone_key(n, p):
    answers = {
        2: {1: "a", 2: "b", 3: "c"},
        3: {1: "d", 2: "e", 3: "f"},
        4: {1: "g", 2: "h", 3: "i"},
        5: {1: "j", 2: "k", 3: "l"},
        6: {1: "m", 2: "n", 3: "o"},
        7: {1: "p", 2: "q", 3: "r"},
        8: {1: "s", 2: "t", 3: "u"},
        9: {1: "v", 2: "x", 3: "y"},
    }
    return answers[n][p]


def get_phone_words_rec(n=2):
    if n > 9:
        return []
    if n == 9:
        return [get_phone_key(n, p) for p in range(1, 4)]
    result = []
    for option in get_phone_words_rec(n + 1):
        for p in range(1, 4):
            result.append(get_phone_key(n, p) + option)
    return result


def get_phone_words_stk(n=8):
    prv_st = [get_phone_key(n, p) for p in range(1, 4)]
    cur_st = []
    while n >= 2:
        while len(prv_st) > 0:
            prv_seq = prv_st.pop()
            for p in range(1, 4):
                cur_seq = get_phone_key(n, p) + prv_seq
                cur_st.append(cur_seq)
        cur_st, prv_st = prv_st, cur_st
        n -= 1
    return prv_st
