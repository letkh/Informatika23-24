for A in range(1, 101):
    k = 0
    for x in range(1, 1000):
        if ((x % 2 == 0) <= (x % 3 != 0)) or (x + A >= 80):
            k += 1
    if k == 999:
        print(A)
        break