# https://www.geeksforgeeks.org/c-program-for-tower-of-hanoi/
def hanoi3(n, src="A", dst="C", piv="B"):
    if n == 0:
        return
    hanoi3(n - 1, src, piv, dst)
    print("Move disk {i} from {s} to {d}".format(i=n, s=src, d=dst))
    hanoi3(n - 1, piv, dst, src)


# https://www.geeksforgeeks.org/recursive-tower-hanoi-using-4-pegs-rods/
def hanoi4(n, src="A", dst="D", piv1="B", piv2="C"):
    if n == 0:
        return
    if n == 1:
        print("Move disk 1 from {s} to {d}".format(s=src, d=dst))
        return
    hanoi4(n - 2, src, piv1, dst, piv2)
    print("Move disk {i} from {s} to {d}".format(i=n - 1, s=src, d=piv2))
    print("Move disk {i} from {s} to {d}".format(i=n, s=src, d=dst))
    print("Move disk {i} from {s} to {d}".format(i=n - 1, s=piv2, d=dst))
    hanoi4(n - 2, piv1, dst, src, piv2)
