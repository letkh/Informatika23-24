def f(n):
    n_bin = format(n, 'b')
    s = ''
    if n % 8 == 0:
        s = f'{n_bin}{n_bin[-2:]}'
    else:
        ost = format((n % 8 * 2), 'b')
        s = f'{n_bin}{ost}'
    return int(s, 2)
a = []
for n in range(1, 10000):
    if f(n) > 3000:
        a.append(n)
print(min(a))