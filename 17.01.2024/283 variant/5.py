def six(n):
    s = ''
    while n > 0:
        s = str(n % 6) + s
        n //= 6
    return s
def f(n):
    n_mod = six(n)
    s = ''
    if n % 3 == 0:
        s = f'{n_mod[:2]}{n_mod}'
    else:
        ost = six(n % 3 * 10)
        s = f'{n_mod}{ost}'
    return int(s, 6)
a = []
for n in range(1, 1000):
    if f(n) > 680:
        a.append(f(n))
print(min(a))