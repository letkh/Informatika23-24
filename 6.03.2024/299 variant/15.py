def f(x, a):
    return (x % 10 == 0) and (x % 26 == 0) and (x < 300) or (a <= x)


for a in range(1, 1000):
    k = 1
    for x in range(1, 1000):
        if f(x, a) == 0:
            k = 0
        if k == 1:
            print(a)
            break