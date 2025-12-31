# https://www.geeksforgeeks.org/c-program-for-tower-of-hanoi/
def hanoi3(n, src="A", dst="C", piv="B"):
    if n == 0:
        return
    hanoi3(n - 1, src, piv, dst)
    print(f"Move disk {n} from {src} to {dst}")
    hanoi3(n - 1, piv, dst, src)


# https://www.geeksforgeeks.org/recursive-tower-hanoi-using-4-pegs-rods/
def hanoi4(n, src="A", dst="D", piv1="B", piv2="C"):
    if n == 0:
        return
    if n == 1:
        print(f"Move disk 1 from {src} to {dst}")
        return
    hanoi4(n - 2, src, piv1, dst, piv2)
    print(f"Move disk {n - 1} from {src} to {piv2}")
    print(f"Move disk {n} from {src} to {dst}")
    print(f"Move disk {n - 1} from {piv2} to {dst}")
    hanoi4(n - 2, piv1, dst, src, piv2)
