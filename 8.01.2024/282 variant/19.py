def f(x,y,p):
    if x + y >= 275 and p == 3:
        return True
    if x + y < 275 and p == 3:
        return False
    if p % 2 == 1:
        return f(x + 3, y, p+1) and f(x + 7, y, p+1) and f(x * 4, y, p + 1) and f(x, y + 3, p+1) and f(x, y + 7, p+1) and f(x, y * 4, p + 1)
    else:
        return f(x + 3, y, p+1) or f(x + 7, y, p+1) or f(x * 4, y, p + 1) or f(x, y + 3, p+1) or f(x, y + 7, p+1) or f(x, y * 4, p + 1)

for s in range(1, 216):
    if f(58, s, 1) == 1:
        print(s)