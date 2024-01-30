def to5(n):
    s = ''
    while n > 0:
        s = str(n % 5) + s
        n //= 5
    return s


def f(n):
    n_mod = to5(n)
    s = ''
    if int(n_mod) % 25 == 0:
        s += f'{n_mod}{n_mod[-3:]}'
    else:
        ost = to5(int(n_mod) % 25)
        s += f'{n_mod}{ost}'
    return int(s,5)

a = []
for i in range(1, 100000):
    if f(i) > 10000:
        a.append(i)

print(min(a))