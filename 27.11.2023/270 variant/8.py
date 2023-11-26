def f(n):
    s = ''
    while n > 0:
        s = str(n % 7) + s
        n //= 7
    return s

k = 0
for x in range(41104, 564355):
    v = f(x)
    if v.count('4') == 1 and '14' not in v and '34' not in v and '54' not in v and '74' not in v and '94' not in v and \
    '41' not in v and '43' not in v and '45' not in v and '47' not in v and '49' not in v:
        k += 1

print(k)