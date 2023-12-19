import numpy as np 

def divisors(n):
    d=[]
    k=2
    while k*k <= n:
        if n%k == 0:
            d.append(k)
            k2 = n//k
            if k2 > k: d.append(k2)
        k += 1
    return d

for i in range(150000, 200000):
    a = divisors(i)
    if len(a) == 0:
        continue
    if np.cbrt(max(a)) % 1 == 0:
        print(min(a), max(a))
