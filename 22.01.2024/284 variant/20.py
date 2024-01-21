# 123456
# ипвпвп
def f(x, y, p):
    if x ** 2 + y ** 2 >= 13 ** 2 and p == 4:
        return True
    if x ** 2 + y ** 2 < 13 ** 2 and p == 4:
        return False
    if x ** 2 + y ** 2 >= 13 ** 2:
        return False

    if p % 2 == 0:
        return f(x + 3, y, p + 1) and f(x, y + 3, p + 1) and f(x, y + 4, p + 1)
    else:
        return f(x + 3, y, p + 1) or f(x, y + 3, p + 1) or f(x, y + 4, p + 1)


for s in range(1, 12):
    if f(s, 2, 1) == 1:
        print(s)
