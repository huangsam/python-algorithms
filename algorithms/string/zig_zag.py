def zig_zag(content, k):
    """Driver function for zig-zag."""
    frame = [[" "] * len(content) for _ in range(k)]
    _zig_zag_wh(content, frame, 0, 0, direction="down")
    return frame


def _zig_zag_wh(content, frame, x, y, direction="down"):
    """Helper function for zig zag."""
    xn, yn = len(frame[0]), len(frame)

    # Frame fill is complete
    if x >= xn - 1:
        return

    # Fill frame with letters
    if direction == "down":
        while x < xn and y < yn:
            frame[y][x] = content[x]
            x += 1
            y += 1
        _zig_zag_wh(content, frame, x - 1, y - 1, direction="up")
    else:
        while x < xn and y >= 0:
            frame[y][x] = content[x]
            x += 1
            y -= 1
        _zig_zag_wh(content, frame, x - 1, y + 1, direction="down")


def print_frame(frame):
    for row in frame:
        print(" ".join(row))


def main():
    sentence = "thisisazigzag"
    print_frame(zig_zag(sentence, 8))
    print("\n===\n")
    print_frame(zig_zag(sentence, 4))
    print("\n===\n")
    print_frame(zig_zag(sentence, 2))


if __name__ == "__main__":
    main()
