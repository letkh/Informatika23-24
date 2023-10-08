def f(n):
    n_bin = format(n, 'b')
    s = ''
    if n % 2 == 0:
        s = '{}00'.format(n_bin)
    else:
        s = '{}11'.format(n_bin)
    r = int(s, 2)
    return r

print('N R')
for n in range(0, 100):
    if f(n) <= 102:
        print(n, f(n))