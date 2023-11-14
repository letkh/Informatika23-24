def f(n):
    n_bin = format(n, 'b')
    tmp = int(n_bin)
    s = 0
    while tmp > 0:
        s += tmp % 10
        tmp //= 10
    #print(n_bin)
    n_bin = f'{n_bin}{s % 2}'
    #print(n_bin)
    tmp = int(n_bin)
    s = 0
    while tmp > 0:
        s += tmp % 10
        tmp //= 10
    n_bin = f'{n_bin}{s % 2}'
    #print(n_bin)
    return int(n_bin, 2)

for i in range(20):
    if f(i) < 57:
        print(f(i))