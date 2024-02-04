from functools import lru_cache
import sys

sys.setrecursionlimit(10000)
lru_cache(None)
def f(n):
    if n == 1:
        return 1
    if n > 1:
        return n * f(n-1)

print(f(2024) / f(2022))