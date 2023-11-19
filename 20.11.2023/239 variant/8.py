def to6(n):
    s = ''
    while n > 0:
        s = str(n % 6) + s
        n //= 6
    return s
k = 0
for x in range(7776, 46656):
    s = to6(x)
    if s.count('2') == 1 and len(s) == 6:
        if '12' not in s and '32' not in s and '52' not in s and '72' not in s and '92' not in s and \
        '21' not in s and '23' not in s and '25' not in s and '27' not in s and '29' not in s:
            k += 1
print(k)