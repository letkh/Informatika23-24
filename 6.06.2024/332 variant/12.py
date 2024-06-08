import sympy as sp

a = []
for n in range(3, 500):
    s = '5' + '4' * n
    while '54' in s or '444' in s or '44444' in s:
        if '54' in s:
            s = s.replace('54', '64', 1)
        if '444' in s:
            s = s.replace('444', '6', 1)
        if '44444' in s:
            s = s.replace('44444', '55', 1)
    if sp.isprime(sum(map(int, s))):
        a.append(n)
print(min(a))