MAX_VAL = 2 ** 32 - 1


def is_digit(ch):
    return ch in "0123456789"


def is_multiply(ch):
    return ch == "*"


def is_addition(ch):
    return ch == "+"


def stack_machine(operation: str):
    st = []
    try:
        for ch in operation:
            if is_digit(ch):
                st.append(int(ch))
            elif is_multiply(ch):
                result = st.pop() * st.pop()
                if result > MAX_VAL:
                    raise Exception("math overflow")
                st.append(result)
            elif is_addition(ch):
                result = st.pop() + st.pop()
                if result > MAX_VAL:
                    raise Exception("math overflow")
                st.append(result)
    except Exception:
        return -1
    return st.pop()
