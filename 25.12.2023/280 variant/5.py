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
        s = f'{n_mod}{n_mod[-2:]}'
    else:
        ost = to4(n % 4 * 2)
        s = f'{n_mod}{ost}'
    return int(s, 4)
a = []
for n in range(1, 1000):
    if f(n) < 369:
        a.append(n)
print(max(a))