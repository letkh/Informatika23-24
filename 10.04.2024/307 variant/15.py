for a in range(1, 1000):
    if all(((150 <= x <= 200) <= (x % a != 0)) or (130 + a > x) for x in range(10000)):
        print(a)