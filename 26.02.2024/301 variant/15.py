for a in range(1, 1000000):
    if all(x&20777 == 0 or (x&12332 != 0 or x&a != 0) for x in range(1, 100000)):
        print(a); break