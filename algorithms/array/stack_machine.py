from collections import deque

from algorithms.constants import MAX_INT


def stack_machine(operation):
    st = deque()
    try:
        for ch in operation:
            if ch.isdigit():
                st.append(int(ch))
            elif ch == "*":
                result = st.pop() * st.pop()
                if result > MAX_INT:
                    raise OverflowError("math overflow")
                st.append(result)
            elif ch == "+":
                result = st.pop() + st.pop()
                if result > MAX_INT:
                    raise OverflowError("math overflow")
                st.append(result)
    except (OverflowError, IndexError):
        return -1
    return st.pop()


class OverflowError(ValueError):
    pass
