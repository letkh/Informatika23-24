def fdel(n, m):
    if n % m == 0:
        return True
    return False

def isIn(x, a, b):
    if a <= x <= b:
        return True
    return False

for a in range(1, 10000):
    k = 0
    for x in range(200):
        if ( fdel(x, a) or ((isIn(x, 50, 70)) <= (not fdel(x, 16))) ):
            k+=1
        if k == 200:
            print(a)
