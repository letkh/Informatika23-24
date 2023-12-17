def f(n):
    s = ''
    while n > 0:
        s = str(n % 7) + s
        n //= 7
    return s
k = 0

for x in range(1, 100000):
    n = f(x)
    if len(n) != 6:
        continue
    if n[0] in '13579':
        continue
    if n[5] in '02468':
        continue
    if n.count('5') > 1:
        continue
    k += 1

print(k)