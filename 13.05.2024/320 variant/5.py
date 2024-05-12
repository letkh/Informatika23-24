def f(n):
    n2 = n - n % 8 + n % 2
    n2 = format(n2, 'b')
    s = n2 + str(sum(map(int, n2)) % 2)
    s = s + str(sum(map(int, s)) % 2)
    return int(s, 2)
a = []
for n in range(1, 100):
    if f(n) > 97:
        a.append(f(n))
print(min(a))