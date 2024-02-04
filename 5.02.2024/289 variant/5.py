def f(n):
    n_bin = format(n, 'b')
    s = ''
    if n % 3 == 0:
        s = n_bin.replace('0', '11')
    else:
        s = n_bin.replace('1', '10')
    return int(s,2)


a = []
for n in range(1, 10000):
    if f(n) < 161:
        a.append(f(n))
print(max(a))