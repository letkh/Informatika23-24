def f(n):
    n_bin = format(n, 'b')
    s = ''
    if n % 5 == 0:
        s = f'{n_bin}{n_bin[-2:]}'
    else:
        ost = format((n % 5) * 2, 'b')
        s = f'{n_bin}{ost}'
    return int(s,2)
a = []
for n in range(1, 1000):
    if f(n) < 150:
        a.append(n)
print(max(a))