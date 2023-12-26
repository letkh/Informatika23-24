def f(n):
    n_bin = format(n, 'b')
    ost = '00' + format(n % 3, 'b')
    s = f'{n_bin}{ost[-2:]}'
    ost = '000' + format(n % 5, 'b')
    s = f'{s}{ost[-3:]}'
    return int(s, 2)
a = []
for x in range(1, 100000000000000):
    if 1_222_222_222 <= f(x) <= 1_555_555_666:
        a.append(f(x))
    elif f(x) > 1_555_555_666:
        break
print(len(set(a)))