import sys
import functools

sys.setrecursionlimit(10000)
functools.lru_cache(None)

def f(n: int) -> int:
    if n > 3000:
        return 1
    if n <= 3000 and n % 2 == 0:
        return f(n + 1) - n + 1
    if n <= 3000 and n % 2 != 0:
        return f(n + 2) - 2 * n + 2

print(2 * f(39) - 2 * f(34))