for a in range(0, 1000):
    k = 0
    for x in range(200):
        for y in range(200):
            if ( ((3 * x + y) > 48) or (x > y) or ((4 * x + y) < a) ) == 0:
                print(a)
