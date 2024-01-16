def f(a,b,c):
    if a + b > c and a + c > b and b + c > a:
        return 1
    return 0

def t(x, a):
    if not ((f(x, 11, 18) == (not (max(x, 5) > 68))) and (f(x, a, 5))):
        return 1
    return 0

for a in range(1, 1000):
    if all(t(x, a) for x in range(1000)):
        print(a)