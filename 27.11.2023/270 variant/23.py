def f(x, y):
    if x == y:
        return 1
    if x> y or x == 11:
        return 0
    return f(x + 1, y) + f(x * 2, y) + f(x * 3, y)
print(f(5, 19) * f(19, 39))