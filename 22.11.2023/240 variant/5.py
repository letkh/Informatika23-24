def f(n):
    n_bin = format(n, 'b')
    s = ''
    if n % 2 == 0:
        s = f'1{n_bin}00'
    else:
        n_bint = int(n_bin)
        k = 0
        while n_bint > 0:
            k += n_bint % 10
            n_bint //= 10
        ost = format(k, 'b')
        s = f'{n_bin}{ost}'
    return int(s, 2)

for i in range(1, 100):
    if f(i) > 190:
        print(i)