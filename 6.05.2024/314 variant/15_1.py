def f(n, m):
    return n % m == 0

for a in range(1, 10000):
    if all( (not f(x, a)) <= (f(x, 28) <= (not f(x, 49))) for x in range(1, 1000)):
        print(a)