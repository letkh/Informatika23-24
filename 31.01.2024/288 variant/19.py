def f(x, y, p):
    if x + y >= 231 and p == 3: return 1
    if x + y >= 231 and p != 3: return 0
    if x + y < 231 and p == 3: return 0

    return f(x + 4, y, p + 1) or f(x * 3, y, p + 1) or f(x, y + 4, p + 1) or f(x, y * 3, p + 1)


for s in range(1, 217):
    if f(10, s, 1) == 1:
        print(s)