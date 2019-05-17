MAX_VAL = 2 ** 32 - 1


def stack_machine(operation):
    st = []
    try:
        for ch in operation:
            if ch.isdigit():
                st.append(int(ch))
            elif ch == "*":
                result = st.pop() * st.pop()
                if result > MAX_VAL:
                    raise OverflowError("math overflow")
                st.append(result)
            elif ch == "+":
                result = st.pop() + st.pop()
                if result > MAX_VAL:
                    raise OverflowError("math overflow")
                st.append(result)
    except (OverflowError, IndexError):
        return -1
    return st.pop()


class OverflowError(ValueError):
    pass
