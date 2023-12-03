def to4(n):
    s = ''
    while n > 0:
        s = str(n % 4) + s
        n //= 4
    return s
def f(n):
    n_mod = to4(n)
    s = ''
    if n % 4 == 0:
        s = n_mod + n_mod[-2:]
    else:
        s = n_mod + to4((n % 4) * 2)
    return int(s, 4)

a = []

for n in range(1, 1000):
    if f(n) < 261:
        print(n)
        a.append(n)

print()
print(max(a))

