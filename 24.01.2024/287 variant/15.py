for a in range(301, 10000):
    if all(x % a == 0 or (not(x % 27 == 0) or (not(x % 89 == 0))) for x in range(100)):
        print(a)
        break