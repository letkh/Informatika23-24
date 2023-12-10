def f(n):
    n_bin = format(n, 'b')
    t = n % 3
    ost = '0000'+format(t, 'b')
    s = f'{n_bin}{ost[-2:]}'
    t = int(s,2) % 5
    ost = '0000'+format(t, 'b')
    s = f'{s}{ost[-3:]}'
    return int(s,2)
a = []
for n in range(10000000, 1000000000):
    if 1111111110 <= f(n) <= 1444444416:
        a.append(f(n))
print( len( list( set(a) ) ) )

