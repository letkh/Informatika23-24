def f(n: int) -> int:
    n2 = format(n, 'b')
    s = ''
    if n % 2 == 0:
        s = n2 + '01'
    else:
        s = '1' + n2 + '1'
    return int(s, 2)

for i in range(1, 100):
    if f(i) > 156:
        print(i)
        break