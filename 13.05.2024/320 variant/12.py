import sympy
for n in range(1, 1000):
    s = '>' + '1' * 16 + '2' * n + '3' * 16
    while '>1' in s or '>2' in s or '>3' in s:
        if '>1' in s:
            s = s.replace('>1', '1>', 1)
        if '>2' in s:
            s = s.replace('>2', '>3', 1)
        if '>3' in s:
            s = s.replace('>3', '>1', 1)
    if sympy.isprime(sum(map(int, s[:-1]))):
        print(n)
        break
