def f(n:int) -> int:
    t = [int(x) for x in str(n)]
    res = [t[0]*t[1], t[1]*t[2]]
    sorted(res)
    return int(f'{res[0]}{res[1]}')


a = []
for n in range(100, 1000):
    if f(n) == 240:
        a.append(n)

print(max(a))