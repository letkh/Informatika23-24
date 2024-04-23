def f(n, m):
    return n % m == 0

for a in range(1, 100):
    if not (f(120, a) <= (not f(168, a))):
        print(a)