def f(n: int) -> int:
    n2 = format(n, 'b')
    s = n2 + str((sum(map(int, n2)) % 2))
    s = s + str((sum(map(int, s)) % 2))
    return int(s, 2)
a = []
for i in range(1, 100):
    if f(i) < 71:
        a.append(f(i))
print(max(a))