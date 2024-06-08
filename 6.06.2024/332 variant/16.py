import sys
sys.setrecursionlimit(10000)
def f(n: int) -> int:
    if n <= 45:
        return n + 1
    if n > 45:
        return n * f(n - 3)

print(f(6041) / f(6029))