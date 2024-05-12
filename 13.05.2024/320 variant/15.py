for a in range(1, 1000):
    if all( ((x >= a) or (y>= a) or (x * y <= 270)) for x in range(1, 1000) for y in range(1, 1000)):
        print(a)