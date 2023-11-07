import sys

sys.setrecursionlimit(1500)

def f(n):
    if n < 3:
        return 1
    if n > 2:
        return f(n-1) + f(n-2)
    
print((f(1006) - f(1004)) / f(1005))