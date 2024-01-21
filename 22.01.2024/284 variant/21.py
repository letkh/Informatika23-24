# 123456
# ипвпвп
def f(x, y, p):
    if x ** 2 + y ** 2 >= 13 ** 2 and (p == 3 or p == 5):
        return True
    if x ** 2 + y ** 2 < 13 ** 2 and p == 5:
        return False
    if x ** 2 + y ** 2 >= 13 ** 2:
        return False

    if p % 2 == 1:
        return f(x + 3, y, p + 1) and f(x, y + 3, p + 1) and f(x, y + 4, p + 1)
    else:
        return f(x + 3, y, p + 1) or f(x, y + 3, p + 1) or f(x, y + 4, p + 1)

def f1(x, y, p):
    if x ** 2 + y ** 2 >= 13 ** 2 and p == 3:
        return True
    if x ** 2 + y ** 2 < 13 ** 2 and p == 3:
        return False
    if x ** 2 + y ** 2 >= 13 ** 2:
        return False

    if p % 2 == 1:
        return f1(x + 3, y, p + 1) and f1(x, y + 3, p + 1) and f1(x, y + 4, p + 1)
    else:
        return f1(x + 3, y, p + 1) or f1(x, y + 3, p + 1) or f1(x, y + 4, p + 1)

for s in range(1, 12):
    if f(s, 2, 1) == 1:
        print(s)

for s in range(1, 12):
    if f1(s, 2, 1) == 1:
        print(s)

