def f(n, m):
    if n % m == 0:
        return True
    return False

for a in range(1, 106):
    k = 0
    for x in range(1, 200):
        if ( (f(x, 2) <= (not f(x, 3))) or (x + a >= 100) ):
            k += 1
        if k == 199:
            print(a)