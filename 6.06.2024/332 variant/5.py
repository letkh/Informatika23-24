import numpy as np

def f(n: int) -> int:
    n3 = np.base_repr(n, base=3)
    s = ''
    if n % 3 == 0:
        s = n3 + n3[-2:]
    else:
        s = n3 + np.base_repr(n % 3 * 2, base=3)

    return int(s, 3)

a = []
for i in range(1, 100):
    if f(i) <= 325:
        a.append(f(i))
print(max(a))