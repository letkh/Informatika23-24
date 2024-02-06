def to4(n):
    s = ''
    while n > 0:
        s = str(n % 4) + s
        n //= 4
    return s


def f(n):
    n2 = to4(n)
    s = ''
    if n % 4 == 0:
        s = f'{n2}{n2[-2:]}'
    else:
        ost = to4(n % 4 * 2)
        s = f'{n2}{ost}'
    return int(s, 4)


for n in range(1, 1000):
    if f(n) > 1025:
        print(n)
        break   

