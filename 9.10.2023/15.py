def f(n, m):
    if n % m == 0:
        return 1
    else:
        return 0

for a in range(1, 100000):
    if (not(f(120, a)) <= (not(f(168, a)))):
        print(a)