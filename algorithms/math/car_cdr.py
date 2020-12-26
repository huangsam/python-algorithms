def car(pair):
    def get_first(x, _):
        return x

    return pair(get_first)


def cdr(pair):
    def get_last(_, y):
        return y

    return pair(get_last)


def cons(a, b):
    def pair(f):
        return f(a, b)

    return pair
