for a in range(0, 1000):
    k = 0
    for x in range(200):
        for y in range(200):
            if ( ((x + 2 * y) > 48) or (y > x) or ((x + 3 * y) < a) ) == 0:
                print(a)
