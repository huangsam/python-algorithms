"""
print_tree.py: Prints tree out to standard output.

print_tree(4, false)
--X--
-XXX-
XXXXX
--X--

print_tree(4, true)
--X--
-X-X-
XXXXX
--X--

print_tree(6, false)
----X----
---XXX---
--XXXXX--
-XXXXXXX-
XXXXXXXXX
----X----

print_tree(6, true)
----X----
---X-X---
--X---X--
-X-----X-
XXXXXXXXX
----X----
"""


def print_line(length, index, is_hallow):
    """Print single line of Christmas tree.

    Args:
        length: Length of tree.
        index: Which line we are printing out.
        is_hallow: Whether the tree is hallow or not.
    """
    middle = int(length / 2)
    left_boundary = middle - index
    right_boundary = middle + index
    result = ''
    for i in range(length):
        if middle == index:
            result += 'X'
        elif i > left_boundary and i < right_boundary and is_hallow is False:
            result += 'X'
        elif i == left_boundary or i == right_boundary:
            result += 'X'
        else:
            result += '-'
    print(result)


def print_tree(height, is_hallow):
    """Print Christmas tree of given height.

    Args:
        height: Height of tree.
        is_hallow: Whether the tree is hallow or not.
    """
    length = (height - 2) * 2 + 1
    for i in range(height - 1):
        print_line(length, i, is_hallow)
    print_line(length, 0, is_hallow)


def main():
    print("Hallow\n===")
    print_tree(10, True)
    print("\nNot hallow\n===")
    print_tree(10, False)


if __name__ == '__main__':
    main()
