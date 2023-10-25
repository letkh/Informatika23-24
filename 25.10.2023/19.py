
def f(x, h, m):
    if h == 3 and x >= 34:
        return 1
    if h == 3 and x < 34:
        return 0
    if x >= 34 and h < 3:
        return 0
    if h % 2 == 0:
        if h == 2:
            if m == 1:
                return f(x + 2, h + 1, m) or f(x * 2, h + 1, m)
            elif m == 2:
                return f(x + 1, h + 1, m) or f(x * 2, h + 1, m)
            elif m == 3:
                return f(x + 1, h + 1, m) or f(x + 2, h + 1, m)
    else:
        return f(x + 1, h + 1, 1) and f(x + 2, h + 1, 2) and f(x * 2, h + 1, 3)

for x in range(1, 33):
    if f(x, 1, 0) == 1:
        print(x)