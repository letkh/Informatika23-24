def f(n):
    n_bin = format(n, 'b')
    ost = format(n % 4, 'b')
    s = f'{n_bin}{ost}'
    return int(s, 2)

s = []
for n in range(1, 1001):
    s.append(f(n))
s = sorted(s)
c = 0
for i in range(1, len(s)):
    count = 0
    for j in range(i + 1, len(s)):
        if s[j] - s[i] <= 49:
            count += 1
        else:
            c = max(c, count)
            break
print(c)
