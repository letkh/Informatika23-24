def f(x, a):
    if not((x & 52 != 0) and (x & 36 == 0)) or (not (x & a == 0)):
        return 1
    return 0


for a in range(100):
    if all(f(x, a) for x in range(100)):
        print(a)
