from sys import *
setrecursionlimit(10_000)
def f(n):
    if n == 1: return 3
    return 3 * n + 2 * f(n - 1)

print(f(2024) - 4 * f(2022))