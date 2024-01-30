def f(x, y, p):
    if x + y >= 231 and (p == 3 or p == 5): return 1
    if x + y < 231 and p == 5: return 0
    if x + y >= 231: return 0
    if p % 2 == 0:
        return f(x + 4, y, p + 1) or f(x * 3, y, p + 1) or f(x, y + 4, p + 1) or f(x, y * 3, p + 1)
    else:
        return f(x + 4, y, p + 1) and f(x * 3, y, p + 1) and f(x, y + 4, p + 1) and f(x, y * 3, p + 1)

def f1(x, y, p):
    if x + y >= 231 and p == 3: return 1
    if x + y < 231 and p == 3: return 0
    if x + y >= 231: return 0
    if p % 2 == 0:
        return f1(x + 4, y, p + 1) or f1(x * 3, y, p + 1) or f1(x, y + 4, p + 1) or f1(x, y * 3, p + 1)
    else:
        return f1(x + 4, y, p + 1) and f1(x * 3, y, p + 1) and f1(x, y + 4, p + 1) and f1(x, y * 3, p + 1)


for s in range(1, 217):
    if f(10, s, 1) == 1:
        print(s)
print()
for s in range(1, 217):
    if f1(10, s, 1) == 1:
        print(s)