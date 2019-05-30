# https://algorithms.tutorialhorizon.com/text-justification-problem/
def word_wrap(words, length):
    if len(words) == 0:
        return ""

    # Step 1: Keep track of character counts as cursor moves
    cursor = 1
    chars_cur = length - len(words[0])
    while chars_cur > 0 and cursor < len(words):
        chars_cur -= len(words[cursor]) + 1
        cursor += 1

    # Step 2: Retrieve current and remaining words via cursor
    pointer = cursor - 1 if chars_cur < 0 else cursor
    cur_words = words[:pointer]
    rem_words = words[pointer:]

    # Step 3: Inject proper amount of spacing for current content
    space_count = 0
    cur_total = sum([len(w) for w in cur_words])
    space_count, _ = divmod(length - cur_total, len(cur_words))
    spc_content = "_" * space_count
    cur_content = spc_content.join(words[1:pointer])

    # Step 4: Add additional left-padding if needed
    buf_content = ""
    used_buffer = len(cur_content) + len(words[0])
    while len(buf_content) < length - used_buffer:
        buf_content += "_"
    cur_content = words[0] + buf_content + cur_content

    # Step 5: Join current content with remaining content
    rem_content = word_wrap(rem_words, length)
    return cur_content + "\n" + rem_content if rem_content else cur_content


if __name__ == "__main__":
    words = [
        "hello",
        "world",
        "t" * 6,
        "needs",
        "cleanup",
        "for",
        "a",
        "while",
        "longer",
        "today",
    ]
    length = 20
    result = word_wrap(words, length)
    print(result)
