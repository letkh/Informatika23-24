import sys
sys.setrecursionlimit(3000)
def f(n):
    if n == 1:
        return 1
    if n == 2:
        return 4
    if n > 2:
        return f(n-1) + (n-1) * f(n-2)
print(f(1604)//f(1600))