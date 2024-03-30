def tr(n: int) -> str:
    s = ''
    while n > 0:
        s = str(n%3) + s
        n //= 3
    return s

def f(n: int) -> int:
    res = ''
    if n % 3 == 0:
        res = tr(n) + tr(n)[-2:]
    else:
        ost = n % 3 * 5
        res = tr(n) + tr(ost)
    return int(res, 3)


a = []
for i in range(1, 10000):
    if f(i) < 242:
        a.append(f(i))
print(max(a))
