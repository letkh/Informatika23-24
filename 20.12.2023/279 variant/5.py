def f(n):
    n_bin = format(n, 'b')
    sum = 0
    t = int(n_bin)
    while t > 0:
        sum += t%10
        t //= 10
    ost = '0000' + str(sum % 2)
    s = f'{n_bin}{ost[-2:]}'
    t = int(s)
    while t > 0:
        sum += t%10
        t //= 10
    ost = '0000' + str(sum % 2)
    s = f'{n_bin}{ost[-2:]}'
    return int(s,2)
a = []
for n in range(1, 10000):
    if f(n) > 176:
        a.append(n)
print(min(a))