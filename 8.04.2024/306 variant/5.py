import numpy as np
def f(n: int) -> int:
    n3 = np.base_repr(n, base=3)
    s = f'21{n3}10' if sum(map(int, n3)) % 5 == 0 else f'{np.base_repr(n % 5, base=3)}{n3}'
    return int(s, 3)

for n in range(1, 1000):
    if f(n) > 200:
        print(n)
        break