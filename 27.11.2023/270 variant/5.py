def f(n):
    n_bin = format(n, 'b')
    tmp = int(n_bin)
    c = 0
    s = ''
    while tmp > 0:
        c += tmp % 10
        tmp //= 10
    if c % 2 == 0:
        s = '110' + n_bin[3:] + '10'
    else:
        s = '10' + n_bin[2:] + '101'
    return int(s, 2)
a = []
for n in range(1, 10000):
    if f(n) > 120:
        a.append(n)

print(min(a))