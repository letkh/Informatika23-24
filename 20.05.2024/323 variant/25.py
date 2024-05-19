import math
import sympy

def divisor(n):
    d = []
    for i in range(2, math.ceil(math.sqrt(n))):
        if n % i == 0:
            d.append(i)
            if i != n // i:
                d.append(n // i)
    return sorted(d)[-1] if len(d) > 1 else 3


c = 0
for i in range(450_001, 1_000_000):
    if sympy.isprime(divisor(i)) == 0:
        print(i, divisor(i))
        c += 1
    if c == 6:
        break

