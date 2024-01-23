def f(n):
    n_bin = format(n, 'b')
    s = ''
    if n % 2 == 0:
        s = f'{n_bin}01'
    else:
        s = f'1{n_bin}10'
    return int(s, 2)


for n in range(1, 100):
    if f(n) > 214:
        print(n)
        break
