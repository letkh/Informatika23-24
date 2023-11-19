def f(n):
    n_bin = format(n, 'b')
    s = ''
    if n % 2 == 0:
        s = f'1{n_bin}0'
    else:
        s = f'11{n_bin}11'
    return int(s, 2)

for n in range(1, 100):
    if f(n) > 225:
        print(n)