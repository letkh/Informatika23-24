for a in range(1, 1000):
    if all((134 != 3 * y + x) or (a < x) or (a < y) for x in range(1, 100) for y in range(1, 100)):
        print(a)