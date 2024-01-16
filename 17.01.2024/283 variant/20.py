#1234567
#иепвепв
def f(x,p):
    if x >= 30 and p != 4: return 1
    # if x <= 30 and p != 4: return 0
    if x >= 30: return 0

    return f(x + 1, p + 1) or f(x * 2, p + 1)

for s in range(1, 29):
    if f(s, 1):
        print(s)