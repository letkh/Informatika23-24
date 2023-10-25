def f(n):
    n_bin = format(n, 'b')
    s = n_bin.replace('1', '2')
    s = s.replace('0', '1')
    s = s.replace('2', '0')
    return (n - int(s, 2))

for n in range(10000):
    if (f(n)) == 999:
        print(n)
        break