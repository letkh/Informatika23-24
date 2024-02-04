def f(x, p):
    if x >= 21 and p == 4:
        return True
    if x <= 21 and p == 4:
        return False

    if p % 2 == 0:
        return f(x + 1, p + 1) and f(x * 2, p + 1)
    else:
        return f(x + 1, p + 1) or f(x * 2, p + 1)


for s in range(1, 21):
    if f(s, 1):
        print(s)