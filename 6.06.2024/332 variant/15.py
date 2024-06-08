for a in range(1, 100):
    if all((x > a) or (y > x) or (3 * x + 2 * y < 120) for x in range(1, 100) for y in range(1, 100)):
        print(a)