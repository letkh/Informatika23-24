for x in range(1000000):
    a = 3 * 11 ** 4 + 3 * 11 ** 3 + 6 * 11 ** 2 + 4 * 11 ** 1 + x
    b = x * 12 ** 4 + 7 * 12 ** 3 + 9 * 12 ** 2 + 4 * 12 ** 1 + 6
    c = 5 * 14 ** 4 + 5 * 14 ** 3 + x * 14 ** 2 + 8 * 14 ** 1 + 7
    if a + b == c:
        print(c)