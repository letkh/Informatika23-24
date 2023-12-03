def f(x, p):
    if x >= 202 and p == 4:
        return 1
    if x < 202 and p == 4:
        return 0
    if x >= 202:
        return 0
    if p % 2 == 1:
        return f(x + 1, p + 1) or f(x + 4, p + 1) or f(x * 3, p + 1)
    else:
        return f(x + 1, p + 1) and f(x + 4, p + 1) and f(x * 3, p + 1)
for x in range(1, 202):
    if f(x, 1):
        print(x)