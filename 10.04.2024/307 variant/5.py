import numpy as np
def f(n: int) -> int:
    nm = np.base_repr(n, base=4)
    if nm.count('1') % 2 == 0:
        nm = nm.replace('1', '2')
    else:
        nm += np.base_repr(nm.count('1'), base=4)
    return int(nm, 4)
a = []
for i in range(1, 1000):
    if f(i) <= 179:
        a.append(f(i))

print(max(a))