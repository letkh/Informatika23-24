def f(n, m):
    if n % m == 0:
        return True
    return False

for a in range(1,10000):
    k = 0
    for x in range(200):
        if ( (not f(x, a)) <= (f(x, 18) <= (not f(x, 81))) ) == 1:
            k += 1
        if k == 200:
            print(a)