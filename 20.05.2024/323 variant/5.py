def f(n: int) -> int:
    n2 = format(n, 'b')
    s = n2.replace('1', '11').replace('0', '00')
    return int(s, 2)
res = []
for n in range(1, 100):
    if f(n) > 32:
        res.append(f(n))
print(min(res))