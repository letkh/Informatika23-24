def f(n):
    s = ''
    n_bin = format(n, 'b')
    if n % 2 == 0:
        s = f'{n_bin}00'
    else:
        s = f'{n_bin}10'
    return int(s, 2)

for n in range(1000):
    if (f(n)) > 130:
        print(n)
        break