def f(n, m):
    if n % m == 0:
        return 1
    return 0

for a in range(1, 100000):
    k = 0
    for x in range(1, 100):
        if ( (f(x, a) or ((not f(x, 16)) or (not f(x, 12))) and (a < 40))  ):
            k += 1
        if k == 99:
            print(a)