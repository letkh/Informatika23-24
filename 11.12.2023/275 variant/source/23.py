import sys

sys.setrecursionlimit(50000)
def F(x, y):
    if x == y: return 1
    if x > y or x == 12: return 0
    if x < y: return F(x+1, y) + F(x*2, y) + F(x*x, y)

print(F(3, 25))