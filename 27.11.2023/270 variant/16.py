import sys
sys.setrecursionlimit(3000)
def f(n):
    if n == 1:
        return 1
    if n == 2:
        return 3
    if n > 2:
        return f(n - 1) + n * f(n-2)
print(f(1890) / f(1885))