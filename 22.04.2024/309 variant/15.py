for a in range(1, 1000):
    if all( (((x & 41 != 0) and (x & 33 == 0)) <= (x & a != 0)) for x in range(0, 10000) ):
        print(a)