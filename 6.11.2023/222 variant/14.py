for a in range(10000):
    for x in range(13):
        for y in range(13):
            m = 2 * 15 ** 5 + y * 15 ** 4 + 2 * 15 ** 3 + 3 * 15 ** 2 + x * 15 + 5
            n = 6 * 13 ** 4 + 7 * 13 ** 3 + x * 13 ** 2 + 9 * 13 + y
            if (m + a) % n == 0:
                print(a)
