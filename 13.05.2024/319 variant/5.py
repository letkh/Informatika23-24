def f(n: int) -> int:
    r = format(n - n % 2, 'b')
    if r.count('0') % 2 == 0:
        r = '10' + r[2:] + '1'
    else:
        r = '11' + r[2:] + '0'
    return int(r, 2)

for n in range(1, 100):
    if f(n) > 50:
        print(n)