for a in range(1, 1000):
    if all((a % 40 == 0) and ((780 % x == 0) <= ((a % x != 0) <= (180 % x != 0))) for x in range(1, 100)):
        print(a)
        break