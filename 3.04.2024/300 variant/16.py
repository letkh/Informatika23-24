from functools import lru_cache
import sys
sys.setrecursionlimit(10000)
lru_cache(None)
def f(n: int) -> int:
    if n <= 11:
        return 7
    if n > 11:
        return n - 3 + f(n-1)


print(f(2022) - f(2020))