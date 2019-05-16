MAX_VAL = 2 ** 32 - 1


def is_digit(ch):
    return ch in {"0", "1", "2", "3", "4", "5", "6", "7", "8", "9"}


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
                first = st.pop()
                second = st.pop()
                result = first * second
                if result > MAX_VAL:
                    raise Exception("math overflow")
                st.append(result)
            elif is_addition(ch):
                first = st.pop()
                second = st.pop()
                result = first + second
                if result > MAX_VAL:
                    raise Exception("math overflow")
                st.append(result)
    except Exception:
        return -1
    return st.pop()
