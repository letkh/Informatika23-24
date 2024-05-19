for a in range(100):
    if all(((x < a) and (y < a) and (x * y > 601)) == 0 for x in range(1000) for y in range(1000)):
        print(a)
