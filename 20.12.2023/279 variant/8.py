def to6(n):
    s = ''
    while n > 0:
        s = str(n%6) + s
        n //= 6
    return s
k = 0
for n in range(1, 100000):
    s = to6(n)
    if len(s) != 5:
        continue
    if s.count('4') != 1:
        continue
    if '14' in s or '34' in s or '54' in s or '74' in s or '94' in s or \
    '41' in s or '43' in s or '45' in s or '47' in s or '49' in s:
        continue
    k += 1
print(k)