def f(n: int) -> int:
    n2 = format(n, 'b')
    s = ''
    if n % 2 == 0:
        s = n2 + '00'
    else:
        s = n2 + '11'
    return int(s, 2)


for n in range(1, 100):
    if f(n) < 102:
        print(n)
