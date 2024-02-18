def f(n):
    n_bin = f'{n:b}'
    s = ''
    if n % 2 == 0:
        s = f'{n_bin}{n_bin[-2:]}'
    else:
        s = f'1{n_bin}0'

    return int(s, 2)

for i in range(100):
    if f(i) < 100:
        print(i)