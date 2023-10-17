def d(n, m):
    if n % m == 0:
        return True
    return False

for a in range(1, 1000):
    if (not(d(396, a) <= (not d(180, a)))) == 1:
        print(a)