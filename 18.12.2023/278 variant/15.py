for a in range(1, 100000):
    k = 0
    for x in range(100):
        if ( (x & a == 0) + ((x & 14 != 0) + (x & 17 != 0)) ):
            k += 1
        if k == 100:
            print(a)