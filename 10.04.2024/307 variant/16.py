import sys
sys.setrecursionlimit(10000)
def f(n: int) -> int:
    if n >= 5881:
        return n + 6
    else:
        return n + 4 + f(n+1)


print(f(63) - f(70))