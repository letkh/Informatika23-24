def f(s):
    while '>1' in s or '>2' in s or '>0' in s:
        if '>1' in s:
            s = s.replace('>1', '22>', 1)
        if '>2' in s:
            s = s.replace('>2', '00>', 1)
        if '>0' in s:
            s = s.replace('>0', '11>', 1)
    s = s.replace('>', '1', 1)
    return s

def s(s):
    n = int(s)
    sum = 0
    while n > 0:
        sum += n % 10
        n //= 10
    return sum


for n in range(40, 10000):
    str = '>' + '0' * n + '1' * n + '2' * n
    if s(f(str)) % 100 == 77:
        print(n)
        break
