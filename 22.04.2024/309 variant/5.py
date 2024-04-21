import numpy as np

def f(n: int) -> int:
    s = ''
    n3 = np.base_repr(n, base=3)
    if n % 3 == 0:
        s = '10' + n3[:-3]
    else:
        s = n3 + np.base_repr(sum(map(int, n3)), base=3)
    return int(s, 3)
a = []
for n in range(1, 100):
    if f(n) > 453:
        a.append(f(n))

print(min(a))