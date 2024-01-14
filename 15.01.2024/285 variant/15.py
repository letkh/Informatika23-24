def f(x, a):
    if ((x & 57 > 0) or (x & 99 > 0)) <= (x & a > 0):
        return 1
    return 0
for a in range(1, 1000):
    if all(f(x, a) for x in range(100)):
        print(a)
        break