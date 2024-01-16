#1234567
#иепвепв
def f(x,p):
    if x >= 30 and p == 5: return 1 
    if x >= 30 and p != 5: return 0 
    
    if p % 3 == 2 or p % 3 == 1:
        return f(x + 1, p + 1) or f(x * 2, p + 1)
    else:
        return f(x + 1, p + 1) and f(x * 2, p + 1)


for s in range(1, 30):
    if f(s, 1):
        print(s)
