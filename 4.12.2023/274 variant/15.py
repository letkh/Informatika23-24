for a in range(1, 200):
    k = 0
    for x in range(1, 200):
        for y in range(1, 200):
            if ( (4 * x + y < a) or (x < y) or (22 <= x) ):
                k += 1
            if k == 39601:
                print(a)