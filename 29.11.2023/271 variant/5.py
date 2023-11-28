def f(n):
    n_bin = format(n, 'b')
    s = ''
    tmp = int(n_bin)
    sum = 0
    while tmp > 0:
        sum += tmp % 10
        tmp //= 10
    if sum % 2 == 0:
        s = '10' + n_bin[2:] + '1'
    else:
        s = '11' + n_bin[2:] + '0'
    tmp = int(s)
    sum = 0
    while tmp > 0:
        sum += tmp % 10
        tmp //= 10
    if sum % 2 == 0:
        s = '10' + s[2:] + '1'
    else:
        s = '11' + s[2:] + '0'
    return int(s, 2)
a = []
for n in range(1, 1000):
    if f(n) > 115:
        a.append(f(n))
print(min(a))