def zig_zag(content, k):
    """Driver function for zig-zag."""
    frame = [[" "] * len(content) for _ in range(k)]
    zig_zag_wh(content, frame, 0, 0, direction="down")
    return frame


def zig_zag_wh(content, frame, x, y, direction="down"):
    """Helper function for zig zag."""
    xn, yn = len(frame[0]), len(frame)

    # Used up all the letters
    if x >= xn - 1:
        return

    # Still have letters left to fill in frame
    if direction == "down":
        while x < xn and y < yn:
            frame[y][x] = content[x]
            x += 1
            y += 1
        zig_zag_wh(content, frame, x - 1, y - 1, direction="up")
    else:
        while x < xn and y >= 0:
            frame[y][x] = content[x]
            x += 1
            y -= 1
        zig_zag_wh(content, frame, x - 1, y + 1, direction="down")


def main():
    sentence = "thisisazigzag"
    k = 4
    matrix = zig_zag(sentence, k)
    for row in matrix:
        print(" ".join(row))


if __name__ == "__main__":
    main()
