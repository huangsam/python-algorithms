def findProfession(level, pos):
    bstream = bin(pos - 1)[2:]
    ones = 0
    for bit in bstream:
        if bit == "1":
            ones += 1
    if ones % 2 == 0:
        return "Engineer"
    return "Doctor"
