for a in range(1, 10000):
    if all((x % 20 == 0 <= x % 11 != 0) or (a < 3 * x + 600) for x in range(1, 10000)):
        print(a)